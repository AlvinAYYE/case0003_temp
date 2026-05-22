import hashlib


def stable_hash(value: str) -> str:
    return hashlib.sha256(value.strip().encode("utf-8")).hexdigest()
