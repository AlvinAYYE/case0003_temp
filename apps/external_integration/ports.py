from dataclasses import dataclass
from datetime import datetime
from typing import Protocol


@dataclass(frozen=True, slots=True)
class LineIdentity:
    line_user_id: str


@dataclass(frozen=True, slots=True)
class LineMessageResult:
    line_request_id: str
    accepted: bool = True
    error_summary: str | None = None


@dataclass(frozen=True, slots=True)
class SmsSendResult:
    provider_message_id: str
    accepted: bool = True
    error_summary: str | None = None


@dataclass(frozen=True, slots=True)
class ExternalCustomer:
    external_customer_id: str
    name: str
    mobile_masked: str
    birthday: str | None = None


@dataclass(frozen=True, slots=True)
class ClinicToken:
    access_token_summary: str
    expires_at: datetime


@dataclass(frozen=True, slots=True)
class ClinicDirectoryItem:
    external_id: str
    name: str


@dataclass(frozen=True, slots=True)
class ClinicTreatmentItem:
    treatment_id: str
    name: str
    duration_minutes: int | None = None


@dataclass(frozen=True, slots=True)
class DoctorSchedule:
    doctor_id: str
    starts_at: datetime
    ends_at: datetime


@dataclass(frozen=True, slots=True)
class ClosedPeriod:
    starts_at: datetime
    ends_at: datetime
    reason: str


@dataclass(frozen=True, slots=True)
class ExistingAppointment:
    doctor_id: str
    starts_at: datetime
    ends_at: datetime


@dataclass(frozen=True, slots=True)
class SchedulingSnapshot:
    schedules: list[DoctorSchedule]
    closed_periods: list[ClosedPeriod]
    existing_appointments: list[ExistingAppointment]
    incomplete_reason: str | None = None


@dataclass(frozen=True, slots=True)
class CreateExternalAppointmentRequest:
    external_customer_id: str
    branch_id: str
    treatment_id: str
    doctor_id: str
    starts_at: datetime
    ends_at: datetime
    idempotency_key: str


@dataclass(frozen=True, slots=True)
class CreatedExternalAppointment:
    external_appointment_id: str
    status: str


@dataclass(frozen=True, slots=True)
class ExternalAppointment:
    external_appointment_id: str
    external_customer_id: str
    branch_id: str
    treatment_id: str
    doctor_id: str
    starts_at: datetime
    ends_at: datetime
    status_code: str


@dataclass(frozen=True, slots=True)
class ClinicEventSummary:
    external_event_id: str
    event_type: str
    occurred_at: datetime
    subject_external_id: str
    summary: str


class LineLoginGateway(Protocol):
    def verify_login_token(self, token: str) -> LineIdentity:
        raise NotImplementedError


class LineMessagingGateway(Protocol):
    def send_appointment_created_notification(
        self,
        line_user_id: str,
        appointment_summary: dict[str, object],
    ) -> LineMessageResult:
        raise NotImplementedError

    def send_reminder(
        self,
        line_user_id: str,
        reminder_summary: dict[str, object],
    ) -> LineMessageResult:
        raise NotImplementedError


class SmsOtpGateway(Protocol):
    def send_otp(self, mobile: str, otp_code: str, message: str) -> SmsSendResult:
        raise NotImplementedError


class ClinicAuthGateway(Protocol):
    def get_token(self) -> ClinicToken:
        raise NotImplementedError

    def refresh_token(self, current_token_summary: str) -> ClinicToken:
        raise NotImplementedError


class ClinicCustomerGateway(Protocol):
    def find_by_mobile(self, mobile: str) -> ExternalCustomer | None:
        raise NotImplementedError

    def create_customer(self, name: str, mobile: str, birthday: str | None) -> ExternalCustomer:
        raise NotImplementedError

    def get_customer(self, external_customer_id: str) -> ExternalCustomer | None:
        raise NotImplementedError


class ClinicDirectoryGateway(Protocol):
    def list_branches(self) -> list[ClinicDirectoryItem]:
        raise NotImplementedError

    def list_doctors(self, branch_id: str) -> list[ClinicDirectoryItem]:
        raise NotImplementedError

    def list_departments(self, branch_id: str) -> list[ClinicDirectoryItem]:
        raise NotImplementedError


class ClinicTreatmentGateway(Protocol):
    def list_treatments(self, branch_id: str) -> list[ClinicTreatmentItem]:
        raise NotImplementedError


class ClinicSchedulingGateway(Protocol):
    def get_schedule(
        self,
        branch_id: str,
        starts_at: datetime,
        ends_at: datetime,
    ) -> SchedulingSnapshot:
        raise NotImplementedError


class ClinicAppointmentGateway(Protocol):
    def create_appointment(
        self,
        request: CreateExternalAppointmentRequest,
    ) -> CreatedExternalAppointment:
        raise NotImplementedError

    def list_appointments(self, external_customer_id: str) -> list[ExternalAppointment]:
        raise NotImplementedError

    def get_appointment(self, external_appointment_id: str) -> ExternalAppointment | None:
        raise NotImplementedError


class ClinicEventGateway(Protocol):
    def list_events(self, since: datetime) -> list[ClinicEventSummary]:
        raise NotImplementedError
