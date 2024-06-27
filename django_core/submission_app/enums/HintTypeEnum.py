from django.db.models import TextChoices


class HintTypeEnum(TextChoices):
    AFTER_RUN = "after_run", "до тестирования"
    BEFORE_RUN = "before_run", "после тестирования"
