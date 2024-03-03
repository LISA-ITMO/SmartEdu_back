from django.conf import settings
from langchain.chat_models.gigachat import GigaChat

from dataclasses import dataclass
from enum import Enum

from langchain.schema import SystemMessage
from .prompt_builders import PromptBuilder, get_code_form_submission

class StatusEnum(Enum):
    SUCCESS = "SUCCESS"
    FAILURE = "FAILURE"


class Data():
    # status = {}
    pass


class GigaChatAdapter:

    def __init__(self):
        """
        Here just implement class instance and other auth stuff
        :param api_key:
        """
        self.giga = GigaChat(
            credentials=settings.GIGACHAT_API_KEY,
            verify_ssl_certs=settings.SSL_SERTS)

    def execute(self, prompt):
        """Use api to intract with model"""
        messages = [SystemMessage(content=prompt)]
        res = self.giga(messages)
        data = {}
        data['prompt'] = prompt
        data['answer'] = res.content
        return data


