import pytest

from apps.common.time import utc_now
from apps.external_integration.adapters import (
    FakeClinicAppointmentGateway,
    FakeClinicAuthGateway,
    FakeClinicCustomerGateway,
    FakeClinicDirectoryGateway,
    FakeClinicSchedulingGateway,
    FakeClinicTreatmentGateway,
    FakeLineLoginGateway,
    FakeLineMessagingGateway,
    FakeSmsOtpGateway,
    PendingClinicEventGateway,
)
from apps.external_integration.errors import (
    GatewayAuthError,
    GatewayConflictError,
    GatewayTimeoutError,
    GatewayValidationError,
)
from apps.external_integration.logging import (
    GatewayRequestLogger,
    RequestLogRepository,
    record_gateway_call,
)
from apps.external_integration.ports import CreateExternalAppointmentRequest, ExternalCustomer


def test_gateway_ports_have_fake_adapters_or_pending_isolation() -> None:
    mobile = _mobile()
    line = FakeLineLoginGateway({_token(): "U123"})
    messaging = FakeLineMessagingGateway()
    sms = FakeSmsOtpGateway()
    auth = FakeClinicAuthGateway()
    customer = FakeClinicCustomerGateway(
        {
            mobile: ExternalCustomer(
                external_customer_id="C-existing",
                name="Existing",
                mobile_masked="09*****678",
            )
        }
    )
    directory = FakeClinicDirectoryGateway()
    treatment = FakeClinicTreatmentGateway()
    scheduling = FakeClinicSchedulingGateway()
    appointment = FakeClinicAppointmentGateway()
    pending_events = PendingClinicEventGateway()

    assert line.verify_login_token(_token()).line_user_id == "U123"
    assert messaging.send_appointment_created_notification("U123", {"appointment": "A1"}).accepted
    assert messaging.send_reminder("U123", {"appointment": "A1"}).line_request_id == "line-2"
    assert sms.send_otp(mobile, _otp(), "verification message").accepted
    assert auth.get_token().access_token_summary == "fake-token-summary"
    assert auth.refresh_token("fake-token-summary").access_token_summary.endswith("-1")
    existing_customer = customer.find_by_mobile(mobile)
    assert existing_customer is not None
    assert existing_customer.external_customer_id == "C-existing"

    created_customer = customer.create_customer("New", mobile, "1990-01-01")
    assert customer.get_customer(created_customer.external_customer_id) == created_customer
    assert directory.list_branches()[0].external_id == "branch-1"
    assert directory.list_doctors("branch-1")[0].external_id == "branch-1-doctor-1"
    assert directory.list_departments("branch-1")[0].external_id == "branch-1-department-1"
    assert treatment.list_treatments("branch-1")[0].duration_minutes == 30
    assert scheduling.get_schedule("branch-1", utc_now(), utc_now()).schedules == []

    request = _appointment_request()
    created_appointment = appointment.create_appointment(request)
    assert appointment.list_appointments("C1")[0].external_appointment_id == "A0001"
    assert appointment.get_appointment(created_appointment.external_appointment_id) is not None

    with pytest.raises(GatewayValidationError):
        pending_events.list_events(utc_now())


def test_fake_adapters_convert_auth_timeout_and_slot_conflict() -> None:
    with pytest.raises(GatewayAuthError):
        FakeLineLoginGateway({"valid": "U123"}).verify_login_token("invalid")

    with pytest.raises(GatewayAuthError):
        FakeSmsOtpGateway(failure="auth").send_otp(_mobile(), _otp(), "verification message")

    with pytest.raises(GatewayTimeoutError):
        FakeLineMessagingGateway(failure="timeout").send_reminder("U123", {"appointment": "A1"})

    with pytest.raises(GatewayConflictError) as conflict:
        FakeClinicAppointmentGateway(failure="conflict").create_appointment(_appointment_request())

    assert conflict.value.summary == "slot conflict"


def test_request_log_records_trace_duration_and_timeout_summary() -> None:
    repository = RequestLogRepository()

    def timeout() -> None:
        raise TimeoutError

    with pytest.raises(GatewayTimeoutError) as timeout_error:
        record_gateway_call(
            repository,
            "sms",
            "send_otp",
            timeout,
            {"mobile": _mobile(), "otp": _otp(), "token": _token()},
        )

    log = repository.logs[0]
    assert log.status == "timeout"
    assert log.provider == "sms"
    assert log.operation == "send_otp"
    assert log.trace_id == timeout_error.value.trace_id
    assert log.duration_ms >= 0
    assert log.error_summary == "timeout"


def test_request_log_sanitizes_request_and_error_summary() -> None:
    repository = RequestLogRepository()
    raw_token = _token()
    raw_mobile = _mobile()
    raw_otp = _otp()

    def auth_error() -> None:
        raise GatewayAuthError(
            "line",
            "verify_login_token",
            f"token={raw_token}; mobile={raw_mobile}; otp={raw_otp}",
        )

    with pytest.raises(GatewayAuthError):
        record_gateway_call(
            repository,
            "line",
            "verify_login_token",
            auth_error,
            {
                "mobile": raw_mobile,
                "otp": raw_otp,
                "token": raw_token,
                "provider_payload": {"code": raw_otp, "mobile": raw_mobile},
            },
        )

    log = repository.logs[0]
    serialized_log = f"{log.request_summary} {log.error_summary}"
    assert log.status == "error"
    assert log.request_summary["mobile"] == "09*****678"
    assert log.request_summary["otp"] == "[redacted]"
    assert raw_mobile not in serialized_log
    assert raw_otp not in serialized_log
    assert raw_token not in serialized_log
    assert "provider_payload" in log.request_summary
    assert log.request_summary["provider_payload"] == "[redacted]"


def test_request_log_decorator_records_success() -> None:
    repository = RequestLogRepository()
    logger = GatewayRequestLogger(repository)

    @logger.decorate("clinic", "list_branches", {"payload": {"mobile": _mobile()}})
    def call() -> list[str]:
        return ["branch-1"]

    assert call() == ["branch-1"]

    log = repository.logs[0]
    assert log.status == "success"
    assert log.trace_id
    assert log.request_summary["payload"] == "[redacted]"


def test_fake_adapters_do_not_store_sensitive_values() -> None:
    mobile = _mobile()
    otp = _otp()
    token = _token()
    sms = FakeSmsOtpGateway()
    line = FakeLineLoginGateway({token: "U123"})

    sms.send_otp(mobile, otp, "verification message")
    line.verify_login_token(token)

    assert sms.sent_otps[0].mobile_masked == "09*****678"
    assert mobile not in str(sms.sent_otps)
    assert otp not in str(sms.sent_otps)
    assert token not in str(vars(line))


def _appointment_request() -> CreateExternalAppointmentRequest:
    now = utc_now()
    return CreateExternalAppointmentRequest(
        external_customer_id="C1",
        branch_id="B1",
        treatment_id="T1",
        doctor_id="D1",
        starts_at=now,
        ends_at=now,
        idempotency_key="idem",
    )


def _mobile() -> str:
    return "09" + "1234" + "5678"


def _otp() -> str:
    return "123" + "456"


def _token() -> str:
    return "secret" + "-token"
