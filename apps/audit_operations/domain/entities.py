from dataclasses import dataclass, field
from datetime import UTC, datetime
from enum import StrEnum

from .value_objects import RequestTraceId


def _utc_now() -> datetime:
    return datetime.now(UTC)


class AuditCategory(StrEnum):
    EVENT = "event"
    ERROR = "error"


class ErrorSeverity(StrEnum):
    INFO = "info"
    WARNING = "warning"
    ERROR = "error"
    CRITICAL = "critical"


class OperationalStatus(StrEnum):
    OPEN = "open"
    ACKNOWLEDGED = "acknowledged"
    RESOLVED = "resolved"
    IGNORED = "ignored"


class ApiRequestStatus(StrEnum):
    STARTED = "started"
    SUCCESS = "success"
    ERROR = "error"
    TIMEOUT = "timeout"


@dataclass(frozen=True, slots=True)
class OperationalIssue:
    error_type: str
    summary: str
    severity: ErrorSeverity = ErrorSeverity.ERROR
    status: OperationalStatus = OperationalStatus.OPEN
    provider: str | None = None
    trace_id: RequestTraceId | None = None

    def __post_init__(self) -> None:
        if not self.error_type.strip():
            raise ValueError("error type is required")
        if not self.summary.strip():
            raise ValueError("issue summary is required")


@dataclass(frozen=True, slots=True)
class ApiErrorSummary:
    provider: str
    operation: str
    error_type: str
    summary: str
    trace_id: RequestTraceId
    status_code: int | None = None
    occurred_at: datetime = field(default_factory=_utc_now)

    def __post_init__(self) -> None:
        if not self.provider.strip():
            raise ValueError("provider is required")
        if not self.operation.strip():
            raise ValueError("operation is required")
        if not self.error_type.strip():
            raise ValueError("error type is required")


@dataclass(frozen=True, slots=True)
class AuditLog:
    category: AuditCategory
    action: str
    trace_id: RequestTraceId
    occurred_at: datetime = field(default_factory=_utc_now)
    actor_type: str = "system"
    actor_id: str | None = None
    target_type: str | None = None
    target_id: str | None = None
    message: str = ""
    metadata: dict[str, object] = field(default_factory=dict)
    severity: ErrorSeverity = ErrorSeverity.INFO
    issue_status: OperationalStatus | None = None
    error_type: str | None = None
    provider: str | None = None

    def __post_init__(self) -> None:
        if not self.action.strip():
            raise ValueError("audit action is required")
        if self.category == AuditCategory.ERROR and not self.error_type:
            raise ValueError("error audit log requires error_type")


@dataclass(frozen=True, slots=True)
class ApiRequestLog:
    provider: str
    operation: str
    trace_id: RequestTraceId
    status: ApiRequestStatus
    started_at: datetime = field(default_factory=_utc_now)
    completed_at: datetime | None = None
    duration_ms: int | None = None
    status_code: int | None = None
    error_type: str | None = None
    error_summary: str | None = None
    request_summary: dict[str, object] = field(default_factory=dict)
    response_summary: dict[str, object] = field(default_factory=dict)

    def __post_init__(self) -> None:
        if not self.provider.strip():
            raise ValueError("provider is required")
        if not self.operation.strip():
            raise ValueError("operation is required")
        if self.duration_ms is not None and self.duration_ms < 0:
            raise ValueError("duration_ms cannot be negative")
