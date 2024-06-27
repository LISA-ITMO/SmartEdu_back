from .executors import ConcretePythonCodeExecutor, BaseCodeExecutor, ConcreteNodeExecutor
from .checkers import CodeChecker
from .prompt_builders import PromptBuilder, get_code_form_submission

executor_map = {"python": ConcretePythonCodeExecutor,
                "node": ConcreteNodeExecutor}


def get_executor_by_name(name: str):
    return executor_map.get(name)
