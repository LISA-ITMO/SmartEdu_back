from django.test import TestCase as DjangoTestCase
from .utils import ConcretePythonCodeExecutor, get_executor_by_name
from .models import Submission
from .enums import StatusEnum
from django.contrib.auth import get_user_model
from unittest.mock import patch
from .tasks import run_code_bare, run_code
from django.core.files.base import File
from task_app.models import Task, CodeTask, TestCase
from tempfile import TemporaryFile

User = get_user_model()


class PythonCodeExecutorTest(DjangoTestCase):
    def test_execute(self):
        executor = ConcretePythonCodeExecutor(code="print('hello_world')")
        status_code = executor.execute()
        stdout = executor.get_stdout().read()

        self.assertEqual(status_code, 0)
        self.assertEqual(stdout, b"hello_world\n")

    def test_with_stdin(self):
        executor = ConcretePythonCodeExecutor(code="print(input())")
        status_code = executor.execute(b"123\n")
        stdout = executor.get_stdout().read()

        self.assertEqual(status_code, 0)
        self.assertEqual(stdout, b"123\n")


class CeleryTaskTest(DjangoTestCase):
    @patch("submission_app.tasks.run_code.delay", return_value=None)
    def setUp(self, mock):
        self.user = User.objects.create(email="silly_student@example.com")

        self.task = Task.objects.create(name="simple task!")
        self.code_task = CodeTask.objects.create(
            task=self.task, content="Just read from stdid"
        )
        self.test_case = TestCase.objects.create(
            code_task=self.code_task,
            stdin=File(open("submission_app/test_case/stdin")),
            stdout=File(open("submission_app/test_case/stdout")),
        )
        self.submission = Submission.objects.create(
            user=self.user,
            code_task=self.code_task,
            language="python",
            code="print('hello_world')",
        )

        self.submission_testcases = Submission.objects.create(
            user=self.user,
            code_task=self.code_task,
            language="python",
            code="print(input())",
        )

    def test_task(self):
        run_code_bare(self.submission.pk)
        self.submission.refresh_from_db()
        self.assertEqual(self.submission.output, "hello_world\n")

    def test_run_code_task(self):
        run_code(self.submission_testcases.pk)
        self.submission_testcases.refresh_from_db()
        self.assertEqual(self.submission_testcases.status, StatusEnum.SUCCESS)
