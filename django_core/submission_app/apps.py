from django.apps import AppConfig


class SubmissionAppConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "submission_app"
    verbose_name = "Тесты задач"

    def ready(self):
        from . import signals
