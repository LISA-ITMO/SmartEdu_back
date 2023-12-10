from django.db.models import TextChoices


class StatusEnum(TextChoices):
    PENDING = "PENDING", "Ожидание"
    SUCCESS = "SUCCESS", "Успех"
    ERROR = "ERROR", "Ошибка"