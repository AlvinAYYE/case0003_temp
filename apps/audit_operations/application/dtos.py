from dataclasses import dataclass, field
from datetime import datetime


@dataclass(frozen=True, slots=True)
class BackofficeAuditLogQuery:
    actions: tuple[str, ...] = ()
    provider: str | None = None
    error_type: str | None = None
    occurred_from: datetime | None = None
    occurred_to: datetime | None = None


@dataclass(frozen=True, slots=True)
class AuditLogReadModel:
    category: str
    action: str
    trace_id: str
    occurred_at: datetime
    actor_type: str
    actor_id: str
    target_type: str
    target_id: str
    message: str
    metadata: dict[str, object] = field(default_factory=dict)
    severity: str = ""
    issue_status: str = ""
    error_type: str = ""
    provider: str = ""


@dataclass(frozen=True, slots=True)
class ApiRequestLogReadModel:
    provider: str
    operation: str
    trace_id: str
    status: str
    started_at: datetime
    completed_at: datetime | None
    duration_ms: int | None
    status_code: int | None
    error_type: str
    error_summary: str
    request_summary: dict[str, object] = field(default_factory=dict)
    response_summary: dict[str, object] = field(default_factory=dict)
