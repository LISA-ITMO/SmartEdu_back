from django.conf import settings
from gigachat import GigaChat

from dataclasses import dataclass
from enum import Enum

class StatusEnum(Enum):
    SUCCESS = "SUCCESS"
    FAILURE = "FAILURE"

class Data(dataclass):

    status = {}


class GigaChatAdapter:

    def __init__(self, api_key):
        """
        Here just implement class instance and other auth stuff
        :param api_key:
        """
        pass

    def execute(self, promt: str) -> dict:
        """Use api to intract with model"""

        data = {}
        return data



