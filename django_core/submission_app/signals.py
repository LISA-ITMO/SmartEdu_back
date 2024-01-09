from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Submission
from logging import getLogger
from .tasks import run_code


@receiver(post_save, sender=Submission)
def execute_task(sender, instance, signal, *args, **kwargs):
    """
    This signal handle execute User's code to "Code checker"
    """
    logger = getLogger(__name__)
    if kwargs.get("created"):
        logger.info(f"Start checking submission {instance.pk}")
        run_code.delay(instance.pk)
