from rest_framework.generics import ListAPIView, RetrieveAPIView
from django_filters.rest_framework import DjangoFilterBackend
from .models import Task, TaskType, CodeTask, TestCase
from .paginations import TaskPagination
from .seralizers import (
    TaskSerializer,
    TaskTypeSerializer,
    CodeTaskSerializer,
    TestCaseSerializer,
)
from .filters import TaskFilterSet


class TaskListView(ListAPIView):
    """
    Provides getting list of Task
    Allow filtration by `tags` and `type`
    """

    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    pagination_class = TaskPagination

    filter_backends = [DjangoFilterBackend]
    filterset_class = TaskFilterSet


class TaskTypeListView(ListAPIView):
    """
    Return all types of `Theory`
    """

    queryset = TaskType.objects.all()
    serializer_class = TaskTypeSerializer


class CodeTaskRetrieveView(RetrieveAPIView):
    """
    Returns long description for `Task` by task id
    """

    lookup_field = "task"
    queryset = CodeTask.objects.all()
    serializer_class = CodeTaskSerializer


class TestCaseListView(ListAPIView):
    """
    This view for internal usage with "Code checker" service.
    Returns list of possible test cases by `CodeTask` id
    """

    queryset = TestCase.objects.all()
    lookup_field = "code_task"
    serializer_class = TestCaseSerializer
