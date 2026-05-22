from dataclasses import dataclass
from uuid import uuid4


@dataclass(frozen=True, slots=True)
class RequestTraceId:
    value: str

    def __post_init__(self) -> None:
        value = self.value.strip()
        if not value:
            raise ValueError("trace id is required")
        if len(value) > 128:
            raise ValueError("trace id must be 128 characters or fewer")
        object.__setattr__(self, "value", value)

    @classmethod
    def new(cls) -> "RequestTraceId":
        return cls(str(uuid4()))
