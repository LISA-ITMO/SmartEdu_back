from django.db import models
from django.contrib.auth.models import AbstractUser
from .manager import CustomUserManager
from .enums import UserType


class User(AbstractUser):
    username = None
    email = models.EmailField("Адрес электронной почты", unique=True)
    type = models.CharField(
        "Тип пользователя", max_length=64, choices=UserType.choices, default=UserType.STUDENT
    )
    profile_image = models.ImageField("Изображение профиля", blank=True, null=True)

    REQUIRED_FIELDS = []
    USERNAME_FIELD = "email"

    objects = CustomUserManager()

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"