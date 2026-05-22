from dataclasses import dataclass


@dataclass(slots=True)
class GatewayError(Exception):
    provider: str
    operation: str
    summary: str
    trace_id: str | None = None
    retryable: bool = False

    def __post_init__(self) -> None:
        Exception.__init__(self, self.provider, self.operation, self.summary, self.trace_id)

    def __str__(self) -> str:
        return f"{self.provider}.{self.operation}: {self.summary}"


class GatewayTimeoutError(GatewayError):
    pass


class GatewayAuthError(GatewayError):
    pass


class GatewayValidationError(GatewayError):
    pass


class GatewayConflictError(GatewayError):
    pass
