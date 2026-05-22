from datetime import datetime
from typing import Protocol

from apps.audit_operations.domain import ApiRequestLog, AuditLog


class AuditLogRepository(Protocol):
    def add_event(self, log: AuditLog) -> AuditLog:
        raise NotImplementedError

    def add_error(self, log: AuditLog) -> AuditLog:
        raise NotImplementedError

    def find_by_trace_id(self, trace_id: str) -> list[AuditLog]:
        raise NotImplementedError

    def find_logs(
        self,
        *,
        actions: tuple[str, ...] = (),
        provider: str | None = None,
        error_type: str | None = None,
        occurred_from: datetime | None = None,
        occurred_to: datetime | None = None,
    ) -> list[AuditLog]:
        raise NotImplementedError

    def find_errors(
        self,
        *,
        error_type: str | None = None,
        provider: str | None = None,
        occurred_from: datetime | None = None,
        occurred_to: datetime | None = None,
    ) -> list[AuditLog]:
        raise NotImplementedError


class ApiRequestLogRepository(Protocol):
    def add_request(self, log: ApiRequestLog) -> ApiRequestLog:
        raise NotImplementedError

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
        raise NotImplementedError

    def find_by_trace_id(self, trace_id: str) -> list[ApiRequestLog]:
        raise NotImplementedError

    def find_provider_errors(
        self,
        *,
        provider: str | None = None,
        error_type: str | None = None,
        occurred_from: datetime | None = None,
        occurred_to: datetime | None = None,
    ) -> list[ApiRequestLog]:
        raise NotImplementedError
