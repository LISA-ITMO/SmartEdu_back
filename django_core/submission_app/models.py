from django.db import models
from .enums import StatusEnum, LanguageEnum


class Submission(models.Model):

    """Model that represent submission and checking task"""

    user = models.ForeignKey(
        "user_app.User",
        null=True,
        on_delete=models.SET_NULL,
        related_name="submissions",
    )

    code_task = models.ForeignKey(
        "task_app.CodeTask",
        null=True,
        on_delete=models.SET_NULL,
        related_name="submissions",
    )

    language = models.CharField(
        verbose_name="Язык программирования",
        max_length=64,
        choices=LanguageEnum.choices,
    )

    code = models.TextField(blank=True)

    status = models.CharField(
        verbose_name="Статус",
        max_length=64,
        choices=StatusEnum.choices,
        default=StatusEnum.PENDING,
    )

    output = models.TextField(null=True)

    worker_uuid = models.CharField(max_length=1024, verbose_name="UUID задачи воркера")

    class Meta:
        verbose_name = "Результат тестирования"
        verbose_name_plural = "Результаты тестирований"
