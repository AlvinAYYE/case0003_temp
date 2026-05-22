from collections.abc import Mapping, Sequence
from typing import Any

SENSITIVE_KEYS = {
    "otp",
    "code",
    "token",
    "password",
    "secret",
    "payload",
    "line_user_id",
    "line_user",
}


def mask_mobile(mobile: str) -> str:
    digits = "".join(char for char in mobile if char.isdigit())
    if len(digits) <= 5:
        return "***"
    return f"{digits[:2]}{'*' * (len(digits) - 5)}{digits[-3:]}"


def sanitize_text(text: str) -> str:
    return text if len(text) <= 12 else f"{text[:4]}...{text[-4:]}"


def sanitize_payload(value: Any) -> Any:
    if isinstance(value, Mapping):
        cleaned: dict[str, Any] = {}
        for key, item in value.items():
            normalized = str(key).lower()
            if "mobile" in normalized or "phone" in normalized:
                cleaned[str(key)] = mask_mobile(str(item))
            elif any(sensitive in normalized for sensitive in SENSITIVE_KEYS):
                cleaned[str(key)] = "[redacted]"
            else:
                cleaned[str(key)] = sanitize_payload(item)
        return cleaned
    if isinstance(value, str):
        return sanitize_text(value)
    if isinstance(value, Sequence) and not isinstance(value, bytes | bytearray):
        return [sanitize_payload(item) for item in value]
    return value
