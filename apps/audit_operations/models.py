from django.db import models


class AuditLogModel(models.Model):
    category = models.CharField(max_length=32)
    actor_type = models.CharField(max_length=64, blank=True)
    actor_id = models.CharField(max_length=128, blank=True)
    action = models.CharField(max_length=128)
    target_type = models.CharField(max_length=128, blank=True)
    target_id = models.CharField(max_length=128, blank=True)
    trace_id = models.CharField(max_length=128, db_index=True)
    severity = models.CharField(max_length=32)
    issue_status = models.CharField(max_length=32, blank=True)
    error_type = models.CharField(max_length=128, blank=True, db_index=True)
    provider = models.CharField(max_length=64, blank=True, db_index=True)
    message = models.CharField(max_length=512, blank=True)
    metadata = models.JSONField(default=dict)
    occurred_at = models.DateTimeField(db_index=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "audit_logs"
        indexes = [
            models.Index(fields=["action", "occurred_at"], name="audit_log_action_time_idx"),
            models.Index(
                fields=["provider", "error_type", "occurred_at"],
                name="audit_log_provider_error_idx",
            ),
        ]


class ApiRequestLogModel(models.Model):
    provider = models.CharField(max_length=64, db_index=True)
    operation = models.CharField(max_length=128)
    trace_id = models.CharField(max_length=128, db_index=True)
    status = models.CharField(max_length=32)
    status_code = models.PositiveIntegerField(null=True, blank=True)
    duration_ms = models.PositiveIntegerField(null=True, blank=True)
    error_type = models.CharField(max_length=128, blank=True, db_index=True)
    error_summary = models.CharField(max_length=512, blank=True)
    request_summary = models.JSONField(default=dict)
    response_summary = models.JSONField(default=dict)
    started_at = models.DateTimeField(db_index=True)
    completed_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "api_request_logs"
        indexes = [
            models.Index(
                fields=["provider", "status", "started_at"],
                name="audit_req_provider_status_idx",
            ),
            models.Index(
                fields=["provider", "error_type", "started_at"],
                name="audit_req_provider_error_idx",
            ),
        ]
