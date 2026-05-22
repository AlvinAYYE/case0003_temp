from datetime import datetime

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
from apps.audit_operations.models import ApiRequestLogModel, AuditLogModel


class DjangoAuditLogRepository:
    def __init__(self, masking_policy: SensitiveDataMaskingPolicy | None = None) -> None:
        self._masking_policy = masking_policy or SensitiveDataMaskingPolicy()

    def add_event(self, log: AuditLog) -> AuditLog:
        return self._create(log)

    def add_error(self, log: AuditLog) -> AuditLog:
        return self._create(log)

    def find_by_trace_id(self, trace_id: str) -> list[AuditLog]:
        return [self._to_domain(model) for model in self._base_query().filter(trace_id=trace_id)]

    def find_logs(
        self,
        *,
        actions: tuple[str, ...] = (),
        provider: str | None = None,
        error_type: str | None = None,
        occurred_from: datetime | None = None,
        occurred_to: datetime | None = None,
    ) -> list[AuditLog]:
        query = self._base_query()
        if actions:
            query = query.filter(action__in=actions)
        if provider:
            query = query.filter(provider=provider)
        if error_type:
            query = query.filter(error_type=error_type)
        if occurred_from:
            query = query.filter(occurred_at__gte=occurred_from)
        if occurred_to:
            query = query.filter(occurred_at__lte=occurred_to)
        return [self._to_domain(model) for model in query]

    def find_errors(
        self,
        *,
        error_type: str | None = None,
        provider: str | None = None,
        occurred_from: datetime | None = None,
        occurred_to: datetime | None = None,
    ) -> list[AuditLog]:
        query = self._base_query().filter(category=AuditCategory.ERROR.value)
        if error_type:
            query = query.filter(error_type=error_type)
        if provider:
            query = query.filter(provider=provider)
        if occurred_from:
            query = query.filter(occurred_at__gte=occurred_from)
        if occurred_to:
            query = query.filter(occurred_at__lte=occurred_to)
        return [self._to_domain(model) for model in query]

    def _create(self, log: AuditLog) -> AuditLog:
        sanitized_metadata = self._masking_policy.sanitize_mapping(log.metadata)
        model = AuditLogModel.objects.create(
            category=log.category.value,
            actor_type=log.actor_type,
            actor_id=self._masking_policy.sanitize_identifier(log.actor_type, log.actor_id),
            action=log.action,
            target_type=log.target_type or "",
            target_id=self._masking_policy.sanitize_identifier(log.target_type, log.target_id),
            trace_id=log.trace_id.value,
            severity=log.severity.value,
            issue_status=log.issue_status.value if log.issue_status else "",
            error_type=log.error_type or "",
            provider=log.provider or "",
            message=self._masking_policy.sanitize_text(log.message),
            metadata=sanitized_metadata,
            occurred_at=log.occurred_at,
        )
        return self._to_domain(model)

    def _base_query(self):
        return AuditLogModel.objects.order_by("occurred_at", "id")

    def _to_domain(self, model: AuditLogModel) -> AuditLog:
        return AuditLog(
            category=AuditCategory(model.category),
            action=model.action,
            trace_id=RequestTraceId(model.trace_id),
            occurred_at=model.occurred_at,
            actor_type=model.actor_type,
            actor_id=model.actor_id or None,
            target_type=model.target_type or None,
            target_id=model.target_id or None,
            message=model.message,
            metadata=model.metadata,
            severity=ErrorSeverity(model.severity),
            issue_status=OperationalStatus(model.issue_status) if model.issue_status else None,
            error_type=model.error_type or None,
            provider=model.provider or None,
        )


class DjangoApiRequestLogRepository:
    def __init__(self, masking_policy: SensitiveDataMaskingPolicy | None = None) -> None:
        self._masking_policy = masking_policy or SensitiveDataMaskingPolicy()

    def add_request(self, log: ApiRequestLog) -> ApiRequestLog:
        model = ApiRequestLogModel.objects.create(
            provider=log.provider,
            operation=log.operation,
            trace_id=log.trace_id.value,
            status=log.status.value,
            status_code=log.status_code,
            duration_ms=log.duration_ms,
            error_type=log.error_type or "",
            error_summary=self._sanitize_optional_text(log.error_summary),
            request_summary=self._masking_policy.sanitize_mapping(log.request_summary),
            response_summary=self._masking_policy.sanitize_mapping(log.response_summary),
            started_at=log.started_at,
            completed_at=log.completed_at,
        )
        return self._to_domain(model)

    def update_response(
        self,
        *,
        trace_id: str,
        status: str,
        status_code: int | None = None,
        duration_ms: int | None = None,
        error_type: str | None = None,
        error_summary: str | None = None,
        response_summary: dict[str, object] | None = None,
        completed_at: datetime | None = None,
        provider: str | None = None,
        operation: str | None = None,
    ) -> ApiRequestLog:
        query = ApiRequestLogModel.objects.filter(trace_id=trace_id)
        if provider:
            query = query.filter(provider=provider)
        if operation:
            query = query.filter(operation=operation)
        model = query.order_by("-started_at", "-id").first()
        if model is None:
            raise LookupError(f"api request log not found for trace id {trace_id}")
        model.status = status
        model.status_code = status_code
        model.duration_ms = duration_ms
        model.error_type = error_type or ""
        model.error_summary = self._sanitize_optional_text(error_summary)
        model.response_summary = self._masking_policy.sanitize_mapping(response_summary or {})
        model.completed_at = completed_at
        model.save(
            update_fields=[
                "status",
                "status_code",
                "duration_ms",
                "error_type",
                "error_summary",
                "response_summary",
                "completed_at",
            ]
        )
        return self._to_domain(model)

    def find_by_trace_id(self, trace_id: str) -> list[ApiRequestLog]:
        return [self._to_domain(model) for model in self._base_query().filter(trace_id=trace_id)]

    def find_provider_errors(
        self,
        *,
        provider: str | None = None,
        error_type: str | None = None,
        occurred_from: datetime | None = None,
        occurred_to: datetime | None = None,
    ) -> list[ApiRequestLog]:
        query = self._base_query().filter(
            status__in=[ApiRequestStatus.ERROR.value, ApiRequestStatus.TIMEOUT.value]
        )
        if provider:
            query = query.filter(provider=provider)
        if error_type:
            query = query.filter(error_type=error_type)
        if occurred_from:
            query = query.filter(started_at__gte=occurred_from)
        if occurred_to:
            query = query.filter(started_at__lte=occurred_to)
        return [self._to_domain(model) for model in query]

    def _base_query(self):
        return ApiRequestLogModel.objects.order_by("started_at", "id")

    def _sanitize_optional_text(self, value: str | None) -> str:
        return self._masking_policy.sanitize_text(value) if value else ""

    def _to_domain(self, model: ApiRequestLogModel) -> ApiRequestLog:
        return ApiRequestLog(
            provider=model.provider,
            operation=model.operation,
            trace_id=RequestTraceId(model.trace_id),
            status=ApiRequestStatus(model.status),
            started_at=model.started_at,
            completed_at=model.completed_at,
            duration_ms=model.duration_ms,
            status_code=model.status_code,
            error_type=model.error_type or None,
            error_summary=model.error_summary or None,
            request_summary=model.request_summary,
            response_summary=model.response_summary,
        )
