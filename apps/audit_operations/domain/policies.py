import re
from collections.abc import Mapping, Sequence

from apps.common.masking import mask_mobile


class SensitiveDataMaskingPolicy:
    _mobile_pattern = re.compile(r"(?<!\d)(09\d{8})(?!\d)")
    _otp_context_pattern = re.compile(
        r"(?i)\b(otp|verification\s*code|one[-_\s]*time\s*password)\s*[:=：]?\s*\d{4,8}\b"
    )
    _chinese_otp_pattern = re.compile(r"(驗證碼|一次性密碼)\s*[:=：]?\s*\d{4,8}")
    _secret_assignment_pattern = re.compile(
        r"(?i)\b(token|access_token|refresh_token|password|passwd|secret|authorization)"
        r"\s*[:=：]\s*[^,\s;]+"
    )
    _line_user_pattern = re.compile(r"\bU[0-9a-fA-F]{20,}\b")

    _mobile_key_parts = ("mobile", "phone", "tel", "手機", "電話")
    _otp_keys = {"otp", "otp_code", "verification_code", "one_time_password", "驗證碼"}
    _secret_key_parts = (
        "token",
        "password",
        "passwd",
        "secret",
        "authorization",
        "credential",
        "api_key",
    )
    _payload_key_parts = (
        "payload",
        "provider_payload",
        "external_payload",
        "raw_payload",
        "raw_request",
        "raw_response",
        "request_body",
        "response_body",
    )
    _line_user_key_parts = (
        "line_user",
        "line_uid",
        "line_profile",
        "line_display",
        "line_picture",
    )
    _medical_key_parts = ("medical_record", "chart", "diagnosis", "病歷", "診斷")

    def sanitize_mapping(self, value: Mapping[str, object]) -> dict[str, object]:
        sanitized = self.sanitize_value(value)
        if isinstance(sanitized, dict):
            return sanitized
        return {}

    def sanitize_value(self, value: object, key: str | None = None) -> object:
        normalized_key = self._normalize_key(key)
        if normalized_key and self._should_redact_key(normalized_key, value):
            return "[redacted]"
        if normalized_key and self._has_key_part(normalized_key, self._mobile_key_parts):
            return self._sanitize_mobile_value(value)
        if normalized_key and self._has_key_part(normalized_key, self._line_user_key_parts):
            return "[redacted]"

        if isinstance(value, Mapping):
            return {
                str(item_key): self.sanitize_value(item_value, str(item_key))
                for item_key, item_value in value.items()
            }
        if isinstance(value, str):
            return self.sanitize_text(value)
        if isinstance(value, Sequence) and not isinstance(value, str | bytes | bytearray):
            return [self.sanitize_value(item) for item in value]
        return value

    def sanitize_text(self, text: str) -> str:
        sanitized = self._mobile_pattern.sub(lambda match: mask_mobile(match.group(1)), text)
        sanitized = self._otp_context_pattern.sub(
            lambda match: f"{match.group(1)} [redacted]", sanitized
        )
        sanitized = self._chinese_otp_pattern.sub(
            lambda match: f"{match.group(1)} [redacted]", sanitized
        )
        sanitized = self._secret_assignment_pattern.sub(
            lambda match: f"{match.group(1)}=[redacted]", sanitized
        )
        return self._line_user_pattern.sub("[redacted-line-user]", sanitized)

    def sanitize_identifier(self, identifier_type: str | None, value: str | None) -> str:
        if not value:
            return ""
        normalized_type = self._normalize_key(identifier_type)
        if normalized_type and (
            "line" in normalized_type
            or self._has_key_part(normalized_type, self._line_user_key_parts)
        ):
            return "[redacted]"
        return self.sanitize_text(value)

    def _sanitize_mobile_value(self, value: object) -> str:
        if value is None:
            return ""
        text = str(value)
        if "*" in text:
            return self.sanitize_text(text)
        return self.sanitize_text(mask_mobile(text))

    def _should_redact_key(self, normalized_key: str, value: object) -> bool:
        if normalized_key in self._otp_keys or "otp" in normalized_key:
            return True
        if normalized_key == "code" and self._looks_like_otp(value):
            return True
        if self._has_key_part(normalized_key, self._secret_key_parts):
            return True
        if self._has_key_part(normalized_key, self._payload_key_parts):
            return True
        if self._has_key_part(normalized_key, self._medical_key_parts):
            return True
        return self._has_key_part(normalized_key, self._line_user_key_parts)

    def _looks_like_otp(self, value: object) -> bool:
        text = str(value)
        return text.isdigit() and 4 <= len(text) <= 8

    def _normalize_key(self, key: str | None) -> str:
        if key is None:
            return ""
        return key.lower().replace("-", "_").strip()

    def _has_key_part(self, normalized_key: str, parts: tuple[str, ...]) -> bool:
        return any(part in normalized_key for part in parts)
