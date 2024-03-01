from django.db import models
from .enums import StatusEnum, LanguageEnum, HintTypeEnum
from .utils import get_executor_by_name


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

    @property
    def code_executor(self):
        return get_executor_by_name(self.language)

    class Meta:
        verbose_name = "Результат тестирования"
        verbose_name_plural = "Результаты тестирований"


class UserPrompt(models.Model):
    """Model that saves user's prompt in db"""

    """It may be redundant!!!"""
    submission = models.ForeignKey(
        Submission,
        verbose_name="Результат тестирования",
        null=True,
        on_delete=models.SET_NULL,
    )
    user = models.ForeignKey(
        "user_app.User",
        verbose_name="Пользователь",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
    )
    hint_type = models.CharField(
        max_length=64, choices=HintTypeEnum.choices, default=HintTypeEnum.AFTER_RUN
    )

    content = models.JSONField(verbose_name="Контент", null=True, blank=True)
