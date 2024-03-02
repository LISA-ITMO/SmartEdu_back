from django_core.django_core.celery import app
from logging import getLogger
from .models import Submission
from .enums import StatusEnum
from .utils import ConcretePythonCodeExecutor, CodeChecker
from openai import OpenAI
from .utils import PromptBuilder, get_code_form_submission
from .models import UserPrompt
from .utils.gigachat_adapter import GigaChatAdapter
from gigachat import GigaChat

from django.conf import settings

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

@app.task()
def send_prompt_by_submission(submission_pk: int):
    """Sends prompt with a code to OpenAI based on submission"""
    giga = GigaChat(credentials=settings.GIGACHAT_API_KEY,
            verify_ssl_certs=settings.SSL_SERTS)
    giga_adapter = GigaChatAdapter(giga)
    # сделать экзмпляр класса

    prompt = PromptBuilder(
        get_code_form_submission(submission_pk)
    )

    response = giga_adapter.execute(prompt)
    # if response is not None:
    #     content = response.model_dump_json()

    if settings.SAVE_PROMPT:
        UserPrompt.objects.create(
            submission_pk=submission_pk,
            content=response
        )
    return response
