from .executors import ConcretePythonCodeExecutor, BaseCodeExecutor
from .checkers import CodeChecker

executor_map = {"python": ConcretePythonCodeExecutor}


def get_executor_by_name(name: str):
    return executor_map.get(name)
