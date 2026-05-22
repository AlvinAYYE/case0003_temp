from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies: list[tuple[str, str]] = []

    operations = [
        migrations.CreateModel(
            name="ApiRequestLogModel",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("provider", models.CharField(db_index=True, max_length=64)),
                ("operation", models.CharField(max_length=128)),
                ("trace_id", models.CharField(db_index=True, max_length=128)),
                ("status", models.CharField(max_length=32)),
                ("status_code", models.PositiveIntegerField(blank=True, null=True)),
                ("duration_ms", models.PositiveIntegerField(blank=True, null=True)),
                ("error_type", models.CharField(blank=True, db_index=True, max_length=128)),
                ("error_summary", models.CharField(blank=True, max_length=512)),
                ("request_summary", models.JSONField(default=dict)),
                ("response_summary", models.JSONField(default=dict)),
                ("started_at", models.DateTimeField(db_index=True)),
                ("completed_at", models.DateTimeField(blank=True, null=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
            ],
            options={
                "db_table": "api_request_logs",
                "indexes": [
                    models.Index(
                        fields=["provider", "status", "started_at"],
                        name="audit_req_provider_status_idx",
                    ),
                    models.Index(
                        fields=["provider", "error_type", "started_at"],
                        name="audit_req_provider_error_idx",
                    ),
                ],
            },
        ),
        migrations.CreateModel(
            name="AuditLogModel",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("category", models.CharField(max_length=32)),
                ("actor_type", models.CharField(blank=True, max_length=64)),
                ("actor_id", models.CharField(blank=True, max_length=128)),
                ("action", models.CharField(max_length=128)),
                ("target_type", models.CharField(blank=True, max_length=128)),
                ("target_id", models.CharField(blank=True, max_length=128)),
                ("trace_id", models.CharField(db_index=True, max_length=128)),
                ("severity", models.CharField(max_length=32)),
                ("issue_status", models.CharField(blank=True, max_length=32)),
                ("error_type", models.CharField(blank=True, db_index=True, max_length=128)),
                ("provider", models.CharField(blank=True, db_index=True, max_length=64)),
                ("message", models.CharField(blank=True, max_length=512)),
                ("metadata", models.JSONField(default=dict)),
                ("occurred_at", models.DateTimeField(db_index=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
            ],
            options={
                "db_table": "audit_logs",
                "indexes": [
                    models.Index(
                        fields=["action", "occurred_at"],
                        name="audit_log_action_time_idx",
                    ),
                    models.Index(
                        fields=["provider", "error_type", "occurred_at"],
                        name="audit_log_provider_error_idx",
                    ),
                ],
            },
        ),
    ]
