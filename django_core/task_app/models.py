from django.db import models
from .enums import StatusEnum, LanguageEnum


class Submission(models.Model):

    """Model that represent submission and checking task"""

    user = models.ForeignKey("user_app.User",
                             on_delete=models.SET_NULL,
                             related_name="submissions")

    task = None

    language = models.TextField(verbose_name="Язык программирования",
                                max_length=64,
                                choices=LanguageEnum.choices,)

    code = models.TextField(blank=True)

    status = models.models.CharField(verbose_name="Тип пользователя",
                                     max_length=64,
                                     choices=StatusEnum.choices,
                                     default=StatusEnum.PENDING)

    worker_uuid = models.CharField(max_length=1024,
                                   verbose_name="Номер задачи")
