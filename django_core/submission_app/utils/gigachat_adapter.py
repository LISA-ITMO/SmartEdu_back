from django.conf import settings
from gigachat import GigaChat

from dataclasses import dataclass
from enum import Enum

from langchain.schema import SystemMessage
from .prompt_builders import PromptBuilder, get_code_form_submission

class StatusEnum(Enum):
    SUCCESS = "SUCCESS"
    FAILURE = "FAILURE"


class Data(dataclass):
    status = {}


class GigaChatAdapter:

    def __init__(self):
        """
        Here just implement class instance and other auth stuff
        :param api_key:
        """
        self.giga = GigaChat(
            credentials=settings.GIGACHAT_API_KEY,
            verify_ssl_certs=settings.SSL_SERTS)

    def execute(self, submission_pk) -> dict:
        """Use api to intract with model"""
        prompt = PromptBuilder(get_code_form_submission(submission_pk))
        messages = [SystemMessage(content=prompt)]
        res = self.giga(messages)
        data = {}
        data['prompt'] = prompt
        data['answer'] = res.content
        return data
