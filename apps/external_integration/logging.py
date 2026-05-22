from __future__ import annotations

import re
from collections.abc import Callable
from dataclasses import dataclass, field
from functools import wraps
from time import perf_counter
from typing import Protocol
from uuid import uuid4

from apps.common.masking import mask_mobile, sanitize_payload

from .errors import GatewayError, GatewayTimeoutError

_SENSITIVE_ASSIGNMENT_PATTERN = re.compile(
    r"(?i)\b(otp|code|token|password|secret)\b\s*[:=]\s*[^,\s;]+"
)
_TAIWAN_MOBILE_PATTERN = re.compile(r"\b09\d{8}\b")


@dataclass(frozen=True, slots=True)
class RequestTraceId:
    value: str

    @classmethod
    def new(cls) -> RequestTraceId:
        return cls(value=str(uuid4()))

    @classmethod
    def from_value(cls, value: str) -> RequestTraceId:
        if not value.strip():
            raise ValueError("trace id is required")
        return cls(value=value)

    def __str__(self) -> str:
        return self.value


@dataclass(frozen=True, slots=True)
class ExternalRequestLog:
    provider: str
    operation: str
    trace_id: str
    status: str
    duration_ms: int
    error_summary: str | None = None
    request_summary: dict[str, object] = field(default_factory=dict)


class RequestLogSink(Protocol):
    def add(self, log: ExternalRequestLog) -> None:
        raise NotImplementedError


class RequestLogRepository:
    def __init__(self) -> None:
        self.logs: list[ExternalRequestLog] = []

    def add(self, log: ExternalRequestLog) -> None:
        self.logs.append(log)


def sanitize_error_summary(summary: str | None) -> str | None:
    if summary is None:
        return None
    cleaned = _TAIWAN_MOBILE_PATTERN.sub(lambda match: mask_mobile(match.group(0)), summary)
    cleaned = _SENSITIVE_ASSIGNMENT_PATTERN.sub(
        lambda match: f"{match.group(1)}=[redacted]",
        cleaned,
    )
    return cleaned[:255]


def sanitize_gateway_payload(value: object) -> object:
    return _sanitize_text_recursively(sanitize_payload(value))


def _sanitize_text_recursively(value: object) -> object:
    if isinstance(value, dict):
        return {str(key): _sanitize_text_recursively(item) for key, item in value.items()}
    if isinstance(value, list):
        return [_sanitize_text_recursively(item) for item in value]
    if isinstance(value, str):
        return sanitize_error_summary(value)
    return value


class GatewayRequestLogger:
    def __init__(self, repository: RequestLogSink) -> None:
        self.repository = repository

    def call[T](
        self,
        provider: str,
        operation: str,
        call: Callable[[], T],
        request_summary: dict[str, object] | None = None,
    ) -> T:
        trace_id = RequestTraceId.new().value
        started_at = perf_counter()
        sanitized_request = sanitize_gateway_payload(request_summary or {})
        try:
            result = call()
        except TimeoutError as error:
            duration = _duration_ms(started_at)
            self.repository.add(
                ExternalRequestLog(
                    provider=provider,
                    operation=operation,
                    trace_id=trace_id,
                    status="timeout",
                    duration_ms=duration,
                    error_summary="timeout",
                    request_summary=_as_request_summary(sanitized_request),
                )
            )
            raise GatewayTimeoutError(provider, operation, "timeout", trace_id, True) from error
        except GatewayTimeoutError as error:
            error.trace_id = error.trace_id or trace_id
            self._add_error_log(
                provider,
                operation,
                error.trace_id,
                "timeout",
                started_at,
                error.summary,
                sanitized_request,
            )
            raise
        except GatewayError as error:
            error.trace_id = error.trace_id or trace_id
            self._add_error_log(
                provider,
                operation,
                error.trace_id,
                "error",
                started_at,
                error.summary,
                sanitized_request,
            )
            raise

        duration = _duration_ms(started_at)
        self.repository.add(
            ExternalRequestLog(
                provider=provider,
                operation=operation,
                trace_id=trace_id,
                status="success",
                duration_ms=duration,
                request_summary=_as_request_summary(sanitized_request),
            )
        )
        return result

    def decorate[T](
        self,
        provider: str,
        operation: str,
        request_summary: dict[str, object] | None = None,
    ) -> Callable[[Callable[[], T]], Callable[[], T]]:
        def decorator(call: Callable[[], T]) -> Callable[[], T]:
            @wraps(call)
            def wrapped() -> T:
                return self.call(provider, operation, call, request_summary)

            return wrapped

        return decorator

    def _add_error_log(
        self,
        provider: str,
        operation: str,
        trace_id: str,
        status: str,
        started_at: float,
        error_summary: str,
        request_summary: object,
    ) -> None:
        self.repository.add(
            ExternalRequestLog(
                provider=provider,
                operation=operation,
                trace_id=trace_id,
                status=status,
                duration_ms=_duration_ms(started_at),
                error_summary=sanitize_error_summary(error_summary),
                request_summary=_as_request_summary(request_summary),
            )
        )


def record_gateway_call[T](
    repository: RequestLogSink,
    provider: str,
    operation: str,
    call: Callable[[], T],
    request_summary: dict[str, object] | None = None,
) -> T:
    return GatewayRequestLogger(repository).call(provider, operation, call, request_summary)


def _duration_ms(started_at: float) -> int:
    return int((perf_counter() - started_at) * 1000)


def _as_request_summary(value: object) -> dict[str, object]:
    if isinstance(value, dict):
        return value
    return {"summary": value}
