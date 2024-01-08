from .executors import BaseCodeExecutor


class CodeChecker:
    """Class for checking with Submission model and CodeExecutor's"""

    test_cases = None

    def __init__(self, submission):
        self.submission = submission
        self.executor_class = self.submission.code_executor
        self.test_cases = list(self.submission.code_task.test_cases.all())

    def test(self) -> bool:
        """
        Checks tests, if all tests passes return True
        :return: bool
        """

        executor: BaseCodeExecutor = self.executor_class(self.submission.code)

        for test_case in self.test_cases:
            status_code = executor.execute(self.get_stdin(test_case))

            if not status_code == 0:
                return False
            if not self.compare_stdout(test_case, executor.get_stdout()):
                return False

        return True

    def get_stdin(self, test_case):
        return test_case.stdin.open("rb").read()

    def compare_stdout(self, test_case, stdout):
        if not stdout.read() == test_case.stdout.open("rb").read():
            return False
        return True
