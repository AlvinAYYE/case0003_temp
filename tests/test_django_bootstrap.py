from django.conf import settings
from django.urls import resolve


def test_django_settings_load_expected_bootstrap_apps() -> None:
    assert settings.ROOT_URLCONF == "config.urls"

    expected_apps = {
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
    }
    assert expected_apps.issubset(set(settings.INSTALLED_APPS))


def test_health_url_is_registered() -> None:
    match = resolve("/health/")

    assert match.url_name == "health"
