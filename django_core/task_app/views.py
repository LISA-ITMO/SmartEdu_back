from rest_framework.generics import ListAPIView, RetrieveAPIView, ListCreateAPIView
from rest_framework.viewsets import ModelViewSet
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


class TaskListViewSet(ModelViewSet):
    """
    Provides getting list of Task
    Allow filtration by `tags` and `type`
    """

    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    pagination_class = TaskPagination

    filter_backends = [DjangoFilterBackend]
    filterset_class = TaskFilterSet


class TaskTypeListView(ListCreateAPIView):
    """
    Return all types of `Theory`
    """

    queryset = TaskType.objects.all()
    serializer_class = TaskTypeSerializer


class CodeTaskRetrieveView(RetrieveAPIView):
    """
    Returns `CodeTask` for by `Task` id

    (Now it's return single instance, maybe it would be list in the future)
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
