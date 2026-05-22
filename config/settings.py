from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = "local-dev-only-not-a-production-secret"
DEBUG = True
ALLOWED_HOSTS: list[str] = []
ROOT_URLCONF = "config.urls"
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
USE_TZ = True
TIME_ZONE = "Asia/Taipei"

INSTALLED_APPS = [
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "apps.external_integration",
    "apps.audit_operations",
    "apps.otp_verification",
    "apps.identity_binding",
    "apps.customer_import",
    "apps.scheduling",
    "apps.appointment_snapshot",
    "apps.notification_reminder",
    "apps.booking",
    "apps.backoffice",
]

MIDDLEWARE: list[str] = []

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

TEMPLATES: list[dict[str, object]] = []
