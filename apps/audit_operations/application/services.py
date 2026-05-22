from collections.abc import Callable
from dataclasses import replace
from datetime import UTC, datetime
from time import perf_counter
from typing import TypeVar

from apps.audit_operations.application.dtos import (
    ApiRequestLogReadModel,
    AuditLogReadModel,
    BackofficeAuditLogQuery,
)
from apps.audit_operations.domain import (
    ApiRequestLog,
    ApiRequestStatus,
    AuditCategory,
    AuditLog,
    ErrorSeverity,
    OperationalStatus,
    RequestTraceId,
    SensitiveDataMaskingPolicy,
)
from apps.audit_operations.ports import ApiRequestLogRepository, AuditLogRepository

T = TypeVar("T")


def _utc_now() -> datetime:
    return datetime.now(UTC)


class AuditService:
    def __init__(
        self,
        repository: AuditLogRepository,
        masking_policy: SensitiveDataMaskingPolicy | None = None,
    ) -> None:
        self._repository = repository
        self._masking_policy = masking_policy or SensitiveDataMaskingPolicy()

    def record_event(
        self,
        *,
        action: str,
        trace_id: str | RequestTraceId | None = None,
        actor_type: str = "system",
        actor_id: str | None = None,
        target_type: str | None = None,
        target_id: str | None = None,
        message: str = "",
        metadata: dict[str, object] | None = None,
        occurred_at: datetime | None = None,
    ) -> AuditLog:
        log = AuditLog(
            category=AuditCategory.EVENT,
            action=action,
            trace_id=self._coerce_trace_id(trace_id),
            occurred_at=occurred_at or _utc_now(),
            actor_type=actor_type,
            actor_id=actor_id,
            target_type=target_type,
            target_id=target_id,
            message=message,
            metadata=metadata or {},
        )
        return self._repository.add_event(self._sanitize_audit_log(log))

    def record_error(
        self,
        *,
        action: str,
        error_type: str,
        trace_id: str | RequestTraceId | None = None,
        provider: str | None = None,
        severity: ErrorSeverity = ErrorSeverity.ERROR,
        issue_status: OperationalStatus = OperationalStatus.OPEN,
        actor_type: str = "system",
        actor_id: str | None = None,
        target_type: str | None = None,
        target_id: str | None = None,
        message: str = "",
        metadata: dict[str, object] | None = None,
        occurred_at: datetime | None = None,
    ) -> AuditLog:
        log = AuditLog(
            category=AuditCategory.ERROR,
            action=action,
            trace_id=self._coerce_trace_id(trace_id),
            occurred_at=occurred_at or _utc_now(),
            actor_type=actor_type,
            actor_id=actor_id,
            target_type=target_type,
            target_id=target_id,
            message=message,
            metadata=metadata or {},
            severity=severity,
            issue_status=issue_status,
            error_type=error_type,
            provider=provider,
        )
        return self._repository.add_error(self._sanitize_audit_log(log))

    def _sanitize_audit_log(self, log: AuditLog) -> AuditLog:
        return replace(
            log,
            actor_id=self._masking_policy.sanitize_identifier(log.actor_type, log.actor_id),
            target_id=self._masking_policy.sanitize_identifier(log.target_type, log.target_id),
            message=self._masking_policy.sanitize_text(log.message),
            metadata=self._masking_policy.sanitize_mapping(log.metadata),
        )

    def _coerce_trace_id(self, trace_id: str | RequestTraceId | None) -> RequestTraceId:
        if isinstance(trace_id, RequestTraceId):
            return trace_id
        if trace_id:
            return RequestTraceId(trace_id)
        return RequestTraceId.new()


class ApiRequestLogService:
    def __init__(
        self,
        repository: ApiRequestLogRepository,
        masking_policy: SensitiveDataMaskingPolicy | None = None,
    ) -> None:
        self._repository = repository
        self._masking_policy = masking_policy or SensitiveDataMaskingPolicy()

    def start_request(
        self,
        *,
        provider: str,
        operation: str,
        trace_id: str | RequestTraceId | None = None,
        request_summary: dict[str, object] | None = None,
        started_at: datetime | None = None,
    ) -> ApiRequestLog:
        log = ApiRequestLog(
            provider=provider,
            operation=operation,
            trace_id=self._coerce_trace_id(trace_id),
            status=ApiRequestStatus.STARTED,
            started_at=started_at or _utc_now(),
            request_summary=self._masking_policy.sanitize_mapping(request_summary or {}),
        )
        return self._repository.add_request(log)

    def record_response(
        self,
        *,
        trace_id: str | RequestTraceId,
        status: ApiRequestStatus,
        status_code: int | None = None,
        duration_ms: int | None = None,
        error_type: str | None = None,
        error_summary: str | None = None,
        response_summary: dict[str, object] | None = None,
        completed_at: datetime | None = None,
        provider: str | None = None,
        operation: str | None = None,
    ) -> ApiRequestLog:
        sanitized_response = self._masking_policy.sanitize_mapping(response_summary or {})
        sanitized_error = (
            self._masking_policy.sanitize_text(error_summary) if error_summary is not None else None
        )
        return self._repository.update_response(
            trace_id=self._coerce_trace_id(trace_id).value,
            status=status.value,
            status_code=status_code,
            duration_ms=duration_ms,
            error_type=error_type,
            error_summary=sanitized_error,
            response_summary=sanitized_response,
            completed_at=completed_at or _utc_now(),
            provider=provider,
            operation=operation,
        )

    def record_call(
        self,
        *,
        provider: str,
        operation: str,
        call: Callable[[], T],
        trace_id: str | RequestTraceId | None = None,
        request_summary: dict[str, object] | None = None,
    ) -> T:
        request_log = self.start_request(
            provider=provider,
            operation=operation,
            trace_id=trace_id,
            request_summary=request_summary,
        )
        started = perf_counter()
        try:
            result = call()
        except TimeoutError:
            self.record_response(
                trace_id=request_log.trace_id,
                provider=provider,
                operation=operation,
                status=ApiRequestStatus.TIMEOUT,
                duration_ms=int((perf_counter() - started) * 1000),
                error_type="TIMEOUT",
                error_summary="timeout",
            )
            raise
        except Exception as error:
            self.record_response(
                trace_id=request_log.trace_id,
                provider=provider,
                operation=operation,
                status=ApiRequestStatus.ERROR,
                duration_ms=int((perf_counter() - started) * 1000),
                error_type=error.__class__.__name__,
                error_summary=str(error),
            )
            raise
        self.record_response(
            trace_id=request_log.trace_id,
            provider=provider,
            operation=operation,
            status=ApiRequestStatus.SUCCESS,
            duration_ms=int((perf_counter() - started) * 1000),
        )
        return result

    def _coerce_trace_id(self, trace_id: str | RequestTraceId | None) -> RequestTraceId:
        if isinstance(trace_id, RequestTraceId):
            return trace_id
        if trace_id:
            return RequestTraceId(trace_id)
        return RequestTraceId.new()


class BackofficeAuditQueryService:
    def __init__(
        self,
        audit_repository: AuditLogRepository,
        api_request_repository: ApiRequestLogRepository,
    ) -> None:
        self._audit_repository = audit_repository
        self._api_request_repository = api_request_repository

    def list_audit_logs(self, query: BackofficeAuditLogQuery) -> list[AuditLogReadModel]:
        logs = self._audit_repository.find_logs(
            actions=query.actions,
            error_type=query.error_type,
            provider=query.provider,
            occurred_from=query.occurred_from,
            occurred_to=query.occurred_to,
        )
        return [self._to_audit_read_model(log) for log in logs]

    def list_api_request_logs(
        self, query: BackofficeAuditLogQuery
    ) -> list[ApiRequestLogReadModel]:
        logs = self._api_request_repository.find_provider_errors(
            provider=query.provider,
            error_type=query.error_type,
            occurred_from=query.occurred_from,
            occurred_to=query.occurred_to,
        )
        if query.actions:
            logs = [log for log in logs if log.operation in query.actions]
        return [self._to_api_read_model(log) for log in logs]

    def _to_audit_read_model(self, log: AuditLog) -> AuditLogReadModel:
        return AuditLogReadModel(
            category=log.category.value,
            action=log.action,
            trace_id=log.trace_id.value,
            occurred_at=log.occurred_at,
            actor_type=log.actor_type,
            actor_id=log.actor_id or "",
            target_type=log.target_type or "",
            target_id=log.target_id or "",
            message=log.message,
            metadata=log.metadata,
            severity=log.severity.value,
            issue_status=log.issue_status.value if log.issue_status else "",
            error_type=log.error_type or "",
            provider=log.provider or "",
        )

    def _to_api_read_model(self, log: ApiRequestLog) -> ApiRequestLogReadModel:
        return ApiRequestLogReadModel(
            provider=log.provider,
            operation=log.operation,
            trace_id=log.trace_id.value,
            status=log.status.value,
            started_at=log.started_at,
            completed_at=log.completed_at,
            duration_ms=log.duration_ms,
            status_code=log.status_code,
            error_type=log.error_type or "",
            error_summary=log.error_summary or "",
            request_summary=log.request_summary,
            response_summary=log.response_summary,
        )
