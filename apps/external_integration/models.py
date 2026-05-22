from django.db import models


class ExternalRequestLogModel(models.Model):
    provider = models.CharField(max_length=64)
    operation = models.CharField(max_length=128)
    trace_id = models.CharField(max_length=64)
    status = models.CharField(max_length=32)
    duration_ms = models.PositiveIntegerField()
    error_summary = models.CharField(max_length=255, blank=True)
    request_summary = models.JSONField(default=dict)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "external_request_logs"
