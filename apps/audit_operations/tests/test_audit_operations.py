from datetime import timedelta

import pytest

from apps.audit_operations.application import (
    ApiRequestLogService,
    AuditService,
    BackofficeAuditLogQuery,
    BackofficeAuditQueryService,
)
from apps.audit_operations.domain import ApiRequestStatus, ErrorSeverity
from apps.audit_operations.infrastructure import (
    DjangoApiRequestLogRepository,
    DjangoAuditLogRepository,
)
from apps.audit_operations.models import ApiRequestLogModel, AuditLogModel
from apps.common.time import utc_now

pytestmark = pytest.mark.django_db


def test_audit_log_write_masks_mobile_and_removes_otp() -> None:
    service = AuditService(DjangoAuditLogRepository())

    service.record_event(
        action="otp.sent",
        trace_id="trace-otp",
        actor_type="line_user",
        actor_id="U11111111111111111111111111111111",
        target_type="mobile",
        target_id="0912345678",
        message="OTP: 123456 sent to 0912345678",
        metadata={
            "mobile": "0912345678",
            "otp": "123456",
            "line_user_id": "U22222222222222222222222222222222",
            "note": "驗證碼：123456 發送到 0912345678",
        },
    )

    model = AuditLogModel.objects.get(trace_id="trace-otp")

    assert model.actor_id == "[redacted]"
    assert model.target_id == "09*****678"
    assert model.metadata["mobile"] == "09*****678"
    assert model.metadata["otp"] == "[redacted]"
    assert model.metadata["line_user_id"] == "[redacted]"
    serialized = str(
        {
            "actor_id": model.actor_id,
            "target_id": model.target_id,
            "message": model.message,
            "metadata": model.metadata,
        }
    )
    assert "0912345678" not in serialized
    assert "123456" not in serialized
    assert "U11111111111111111111111111111111" not in serialized
    assert "U22222222222222222222222222222222" not in serialized


def test_api_request_log_write_removes_token_password_and_payload() -> None:
    service = ApiRequestLogService(DjangoApiRequestLogRepository())

    service.start_request(
        provider="clinic",
        operation="create_appointment",
        trace_id="trace-api",
        request_summary={
            "phone": "0912345678",
            "token": "secret-token",
            "password": "plain-password",
            "payload": {"patient": {"mobile": "0912345678", "chart": "full medical payload"}},
            "medical_record": "complete medical chart",
            "headers": {"Authorization": "Bearer abc"},
        },
    )
    service.record_response(
        trace_id="trace-api",
        provider="clinic",
        operation="create_appointment",
        status=ApiRequestStatus.ERROR,
        status_code=500,
        duration_ms=42,
        error_type="AUTH_FAILED",
        error_summary="token=secret-token password=plain-password mobile 0912345678",
        response_summary={
            "provider_payload": {"raw": "full provider payload"},
            "message": "OTP 123456 rejected",
        },
    )

    model = ApiRequestLogModel.objects.get(trace_id="trace-api")

    assert model.request_summary["phone"] == "09*****678"
    assert model.request_summary["token"] == "[redacted]"
    assert model.request_summary["password"] == "[redacted]"
    assert model.request_summary["payload"] == "[redacted]"
    assert model.request_summary["medical_record"] == "[redacted]"
    assert model.request_summary["headers"]["Authorization"] == "[redacted]"
    assert model.response_summary["provider_payload"] == "[redacted]"
    serialized = str(
        {
            "request_summary": model.request_summary,
            "response_summary": model.response_summary,
            "error_summary": model.error_summary,
        }
    )
    assert "secret-token" not in serialized
    assert "plain-password" not in serialized
    assert "full provider payload" not in serialized
    assert "complete medical chart" not in serialized
    assert "0912345678" not in serialized
    assert "123456" not in serialized


def test_trace_id_links_application_error_and_gateway_request_log() -> None:
    trace_id = "trace-booking-failed"
    audit_repository = DjangoAuditLogRepository()
    api_repository = DjangoApiRequestLogRepository()
    audit_service = AuditService(audit_repository)
    api_service = ApiRequestLogService(api_repository)

    api_service.start_request(
        provider="clinic",
        operation="create_appointment",
        trace_id=trace_id,
        request_summary={"mobile": "0912345678"},
    )
    api_service.record_response(
        trace_id=trace_id,
        provider="clinic",
        operation="create_appointment",
        status=ApiRequestStatus.ERROR,
        status_code=409,
        duration_ms=80,
        error_type="SLOT_CONFLICT",
        error_summary="slot conflict for 0912345678",
    )
    audit_service.record_error(
        action="booking.write_failed",
        error_type="SLOT_CONFLICT",
        provider="clinic",
        trace_id=trace_id,
        severity=ErrorSeverity.ERROR,
        metadata={"mobile": "0912345678"},
    )

    audit_logs = audit_repository.find_by_trace_id(trace_id)
    api_logs = api_repository.find_by_trace_id(trace_id)

    assert [log.error_type for log in audit_logs] == ["SLOT_CONFLICT"]
    assert [log.error_type for log in api_logs] == ["SLOT_CONFLICT"]
    assert audit_logs[0].trace_id.value == api_logs[0].trace_id.value


def test_provider_error_query_filters_by_error_type_provider_and_time() -> None:
    repository = DjangoApiRequestLogRepository()
    service = ApiRequestLogService(repository)
    now = utc_now()

    _record_failed_request(
        service,
        trace_id="trace-clinic-auth",
        provider="clinic",
        operation="get_token",
        error_type="AUTH_FAILED",
        started_at=now,
    )
    _record_failed_request(
        service,
        trace_id="trace-line-auth",
        provider="line",
        operation="send_message",
        error_type="AUTH_FAILED",
        started_at=now,
    )
    _record_failed_request(
        service,
        trace_id="trace-old-clinic-auth",
        provider="clinic",
        operation="get_token",
        error_type="AUTH_FAILED",
        started_at=now - timedelta(days=2),
    )

    logs = repository.find_provider_errors(
        provider="clinic",
        error_type="AUTH_FAILED",
        occurred_from=now - timedelta(minutes=5),
        occurred_to=now + timedelta(minutes=5),
    )

    assert [log.trace_id.value for log in logs] == ["trace-clinic-auth"]


def test_backoffice_query_does_not_expose_sensitive_data() -> None:
    audit_repository = DjangoAuditLogRepository()
    api_repository = DjangoApiRequestLogRepository()
    audit_service = AuditService(audit_repository)
    api_service = ApiRequestLogService(api_repository)
    query_service = BackofficeAuditQueryService(audit_repository, api_repository)

    audit_service.record_event(
        action="otp.sent",
        trace_id="trace-backoffice-otp",
        actor_type="line_user",
        actor_id="U33333333333333333333333333333333",
        target_type="mobile",
        target_id="0912345678",
        metadata={"mobile": "0912345678", "otp": "123456"},
    )
    _record_failed_request(
        api_service,
        trace_id="trace-backoffice-line",
        provider="line",
        operation="send_message",
        error_type="AUTH_FAILED",
        started_at=utc_now(),
        request_summary={
            "line_user_id": "U44444444444444444444444444444444",
            "token": "line-token",
        },
    )

    audit_logs = query_service.list_audit_logs(BackofficeAuditLogQuery(actions=("otp.sent",)))
    api_logs = query_service.list_api_request_logs(
        BackofficeAuditLogQuery(provider="line", error_type="AUTH_FAILED")
    )

    serialized = str({"audit_logs": audit_logs, "api_logs": api_logs})
    assert "09*****678" in serialized
    assert "0912345678" not in serialized
    assert "123456" not in serialized
    assert "line-token" not in serialized
    assert "U33333333333333333333333333333333" not in serialized
    assert "U44444444444444444444444444444444" not in serialized


def test_record_call_records_trace_duration_status_and_error_summary() -> None:
    repository = DjangoApiRequestLogRepository()
    service = ApiRequestLogService(repository)

    def timeout() -> None:
        raise TimeoutError("provider timeout for 0912345678")

    with pytest.raises(TimeoutError):
        service.record_call(
            provider="sms",
            operation="send_otp",
            trace_id="trace-timeout",
            request_summary={"mobile": "0912345678", "otp": "123456", "token": "sms-token"},
            call=timeout,
        )

    model = ApiRequestLogModel.objects.get(trace_id="trace-timeout")
    assert model.status == "timeout"
    assert model.duration_ms is not None
    assert model.error_type == "TIMEOUT"
    serialized = str(
        {
            "request_summary": model.request_summary,
            "error_summary": model.error_summary,
        }
    )
    assert "0912345678" not in serialized
    assert "123456" not in serialized
    assert "sms-token" not in serialized


def _record_failed_request(
    service: ApiRequestLogService,
    *,
    trace_id: str,
    provider: str,
    operation: str,
    error_type: str,
    started_at,
    request_summary: dict[str, object] | None = None,
) -> None:
    service.start_request(
        provider=provider,
        operation=operation,
        trace_id=trace_id,
        request_summary=request_summary or {"mobile": "0912345678"},
        started_at=started_at,
    )
    service.record_response(
        trace_id=trace_id,
        provider=provider,
        operation=operation,
        status=ApiRequestStatus.ERROR,
        status_code=500,
        duration_ms=30,
        error_type=error_type,
        error_summary=f"{error_type} for 0912345678",
        completed_at=started_at + timedelta(milliseconds=30),
    )
