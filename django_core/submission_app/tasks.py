from django_core.celery import app
from logging import getLogger
from .models import Submission
from .enums import StatusEnum
from .utils import ConcretePythonCodeExecutor, CodeChecker

logger = getLogger(__name__)


@app.task()
def run_code_bare(submission_pk: int):
    """
    Bare implementation of code checking
    :param submission_pk:
    :return:
    """
    submission = Submission.objects.get(pk=submission_pk)
    executor: ConcretePythonCodeExecutor = submission.code_executor(submission.code)
    logger.info(f"execution for Submission({submission.pk})")
    status_code = executor.execute()
    if status_code != 0:
        submission.status = StatusEnum.ERROR

    submission.output = executor.get_stdout().read().decode("UTF-8")
    logger.info(submission.output)
    submission.save()


@app.task()
def run_code(submission_pk: int):
    """
    Code checking with test cases in db.
    :param submission_pk:
    :return:
    """
    submission = Submission.objects.get(pk=submission_pk)
    checker = CodeChecker(submission)
    if checker.test():
        submission.status = StatusEnum.SUCCESS
    else:
        submission.status = StatusEnum.ERROR

    submission.save()

