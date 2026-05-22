from dataclasses import dataclass
from datetime import UTC, datetime, timedelta
from typing import Literal

from apps.common.hashing import stable_hash
from apps.common.masking import mask_mobile

from .errors import (
    GatewayAuthError,
    GatewayConflictError,
    GatewayError,
    GatewayTimeoutError,
    GatewayValidationError,
)
from .logging import sanitize_error_summary, sanitize_gateway_payload
from .ports import (
    ClinicDirectoryItem,
    ClinicEventSummary,
    ClinicToken,
    ClinicTreatmentItem,
    ClosedPeriod,
    CreatedExternalAppointment,
    CreateExternalAppointmentRequest,
    DoctorSchedule,
    ExistingAppointment,
    ExternalAppointment,
    ExternalCustomer,
    LineIdentity,
    LineMessageResult,
    SchedulingSnapshot,
    SmsSendResult,
)

FakeFailure = Literal["timeout", "auth", "validation", "conflict", "error"]


@dataclass(frozen=True, slots=True)
class FakeLineMessage:
    line_user_hash: str
    operation: str
    request_summary: dict[str, object]


@dataclass(frozen=True, slots=True)
class FakeSmsOtpSend:
    mobile_masked: str
    provider_message_id: str


def gateway_error_from_fake_provider(
    provider: str,
    operation: str,
    failure: FakeFailure,
    summary: str | None = None,
) -> GatewayError:
    safe_summary = sanitize_error_summary(summary or failure) or failure
    if failure == "timeout":
        return GatewayTimeoutError(provider, operation, safe_summary, retryable=True)
    if failure == "auth":
        return GatewayAuthError(provider, operation, safe_summary)
    if failure == "validation":
        return GatewayValidationError(provider, operation, safe_summary)
    if failure == "conflict":
        return GatewayConflictError(provider, operation, safe_summary)
    return GatewayError(provider, operation, safe_summary)


def _raise_if_failed(
    provider: str,
    operation: str,
    failure: FakeFailure | None,
    summary: str | None = None,
) -> None:
    if failure is not None:
        raise gateway_error_from_fake_provider(provider, operation, failure, summary)


class FakeLineLoginGateway:
    def __init__(self, token_to_user: dict[str, str] | None = None) -> None:
        self._token_hash_to_user = {
            stable_hash(token): user_id for token, user_id in (token_to_user or {}).items()
        }

    def verify_login_token(self, token: str) -> LineIdentity:
        line_user_id = self._token_hash_to_user.get(stable_hash(token))
        if line_user_id is None:
            raise GatewayAuthError("line", "verify_login_token", "invalid line token")
        return LineIdentity(line_user_id=line_user_id)


class FakeLineMessagingGateway:
    def __init__(self, failure: FakeFailure | None = None) -> None:
        self.failure = failure
        self.sent_messages: list[FakeLineMessage] = []

    def send_appointment_created_notification(
        self,
        line_user_id: str,
        appointment_summary: dict[str, object],
    ) -> LineMessageResult:
        return self._send(
            "send_appointment_created_notification",
            line_user_id,
            appointment_summary,
        )

    def send_reminder(
        self,
        line_user_id: str,
        reminder_summary: dict[str, object],
    ) -> LineMessageResult:
        return self._send("send_reminder", line_user_id, reminder_summary)

    def send_message(self, line_user_id: str, message: str) -> LineMessageResult:
        return self._send("send_message", line_user_id, {"message": message})

    def _send(
        self,
        operation: str,
        line_user_id: str,
        request_summary: dict[str, object],
    ) -> LineMessageResult:
        _raise_if_failed("line", operation, self.failure, "line message rejected")
        self.sent_messages.append(
            FakeLineMessage(
                line_user_hash=stable_hash(line_user_id),
                operation=operation,
                request_summary=_as_summary_dict(sanitize_gateway_payload(request_summary)),
            )
        )
        return LineMessageResult(line_request_id=f"line-{len(self.sent_messages)}")


class FakeSmsOtpGateway:
    def __init__(self, failure: FakeFailure | None = None) -> None:
        self.failure = failure
        self.sent_otps: list[FakeSmsOtpSend] = []

    def send_otp(self, mobile: str, otp_code: str, message: str) -> SmsSendResult:
        _raise_if_failed("sms", "send_otp", self.failure, "sms rejected")
        provider_message_id = f"sms-{len(self.sent_otps) + 1}"
        self.sent_otps.append(
            FakeSmsOtpSend(
                mobile_masked=mask_mobile(mobile),
                provider_message_id=provider_message_id,
            )
        )
        return SmsSendResult(provider_message_id=provider_message_id)


class FakeClinicAuthGateway:
    def __init__(self, failure: FakeFailure | None = None) -> None:
        self.failure = failure
        self.refresh_count = 0

    def get_token(self) -> ClinicToken:
        _raise_if_failed("clinic", "get_token", self.failure, "clinic auth failed")
        return self._token("fake-token-summary")

    def refresh_token(self, current_token_summary: str) -> ClinicToken:
        _raise_if_failed("clinic", "refresh_token", self.failure, "clinic auth refresh failed")
        self.refresh_count += 1
        return self._token(f"fake-token-summary-refreshed-{self.refresh_count}")

    def _token(self, token_summary: str) -> ClinicToken:
        return ClinicToken(
            access_token_summary=token_summary,
            expires_at=datetime.now(UTC) + timedelta(hours=1),
        )


class FakeClinicCustomerGateway:
    def __init__(
        self,
        customers_by_mobile: dict[str, ExternalCustomer] | None = None,
        failure: FakeFailure | None = None,
    ) -> None:
        self.failure = failure
        self.created_count = 0
        self._customers_by_id: dict[str, ExternalCustomer] = {}
        self._customer_id_by_mobile_hash: dict[str, str] = {}
        for mobile, customer in (customers_by_mobile or {}).items():
            self._customers_by_id[customer.external_customer_id] = customer
            self._customer_id_by_mobile_hash[stable_hash(mobile)] = customer.external_customer_id

    def find_by_mobile(self, mobile: str) -> ExternalCustomer | None:
        _raise_if_failed("clinic", "find_by_mobile", self.failure, "customer query failed")
        customer_id = self._customer_id_by_mobile_hash.get(stable_hash(mobile))
        if customer_id is None:
            return None
        return self._customers_by_id.get(customer_id)

    def create_customer(self, name: str, mobile: str, birthday: str | None) -> ExternalCustomer:
        _raise_if_failed("clinic", "create_customer", self.failure, "customer create failed")
        self.created_count += 1
        customer = ExternalCustomer(
            external_customer_id=f"C{self.created_count:04d}",
            name=name,
            mobile_masked=mask_mobile(mobile),
            birthday=birthday,
        )
        self._customers_by_id[customer.external_customer_id] = customer
        self._customer_id_by_mobile_hash[stable_hash(mobile)] = customer.external_customer_id
        return customer

    def get_customer(self, external_customer_id: str) -> ExternalCustomer | None:
        _raise_if_failed("clinic", "get_customer", self.failure, "customer read failed")
        return self._customers_by_id.get(external_customer_id)


class FakeClinicDirectoryGateway:
    def __init__(self, failure: FakeFailure | None = None) -> None:
        self.failure = failure

    def list_branches(self) -> list[ClinicDirectoryItem]:
        _raise_if_failed("clinic", "list_branches", self.failure, "directory query failed")
        return [ClinicDirectoryItem(external_id="branch-1", name="Main")]

    def list_doctors(self, branch_id: str) -> list[ClinicDirectoryItem]:
        _raise_if_failed("clinic", "list_doctors", self.failure, "directory query failed")
        return [ClinicDirectoryItem(external_id=f"{branch_id}-doctor-1", name="Doctor")]

    def list_departments(self, branch_id: str) -> list[ClinicDirectoryItem]:
        _raise_if_failed("clinic", "list_departments", self.failure, "directory query failed")
        return [ClinicDirectoryItem(external_id=f"{branch_id}-department-1", name="Department")]


class FakeClinicTreatmentGateway:
    def __init__(self, failure: FakeFailure | None = None) -> None:
        self.failure = failure

    def list_treatments(self, branch_id: str) -> list[ClinicTreatmentItem]:
        _raise_if_failed("clinic", "list_treatments", self.failure, "treatment query failed")
        return [
            ClinicTreatmentItem(
                treatment_id=f"{branch_id}-treatment-1",
                name="Treatment",
                duration_minutes=30,
            )
        ]


class FakeClinicSchedulingGateway:
    def __init__(
        self,
        schedules: list[DoctorSchedule] | None = None,
        closed_periods: list[ClosedPeriod] | None = None,
        appointments: list[ExistingAppointment] | None = None,
        incomplete_reason: str | None = None,
        failure: FakeFailure | None = None,
    ) -> None:
        self.schedules = schedules or []
        self.closed_periods = closed_periods or []
        self.appointments = appointments or []
        self.incomplete_reason = incomplete_reason
        self.failure = failure

    def get_schedule(
        self,
        branch_id: str,
        starts_at: datetime,
        ends_at: datetime,
    ) -> SchedulingSnapshot:
        _raise_if_failed("clinic", "get_schedule", self.failure, "scheduling query failed")
        return SchedulingSnapshot(
            schedules=self.schedules,
            closed_periods=self.closed_periods,
            existing_appointments=self.appointments,
            incomplete_reason=self.incomplete_reason,
        )


class FakeClinicAppointmentGateway:
    def __init__(self, failure: FakeFailure | None = None) -> None:
        self.failure = failure
        self.created_requests: list[CreateExternalAppointmentRequest] = []
        self.appointments: dict[str, ExternalAppointment] = {}

    def create_appointment(
        self,
        request: CreateExternalAppointmentRequest,
    ) -> CreatedExternalAppointment:
        _raise_if_failed("clinic", "create_appointment", self.failure, "slot conflict")
        self.created_requests.append(request)
        external_id = f"A{len(self.created_requests):04d}"
        self.appointments[external_id] = ExternalAppointment(
            external_appointment_id=external_id,
            external_customer_id=request.external_customer_id,
            branch_id=request.branch_id,
            treatment_id=request.treatment_id,
            doctor_id=request.doctor_id,
            starts_at=request.starts_at,
            ends_at=request.ends_at,
            status_code="created",
        )
        return CreatedExternalAppointment(external_appointment_id=external_id, status="created")

    def list_appointments(self, external_customer_id: str) -> list[ExternalAppointment]:
        _raise_if_failed("clinic", "list_appointments", self.failure, "appointment query failed")
        return [
            appointment
            for appointment in self.appointments.values()
            if appointment.external_customer_id == external_customer_id
        ]

    def get_appointment(self, external_appointment_id: str) -> ExternalAppointment | None:
        _raise_if_failed("clinic", "get_appointment", self.failure, "appointment read failed")
        return self.appointments.get(external_appointment_id)


class PendingClinicEventGateway:
    def list_events(self, since: datetime) -> list[ClinicEventSummary]:
        raise GatewayValidationError(
            "clinic",
            "list_events",
            "clinic event gateway pending provider confirmation",
        )


def _as_summary_dict(value: object) -> dict[str, object]:
    if isinstance(value, dict):
        return value
    return {"summary": value}
