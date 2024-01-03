from django.urls import path
from .views import (
    CodeTaskRetrieveView,
    TestCaseListView,
    TaskListViewSet,
    TaskTypeListViewSet,
)

urlpatterns = [
    path("tasks", TaskListViewSet.as_view({'get': 'list', 'post': 'create'})),
    path("tasks/<int:task>", TaskListViewSet.as_view({'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'})),
    path("tasks/<int:task>/code-tasks", CodeTaskRetrieveView.as_view()),
    path("tasks/types", TaskTypeListViewSet.as_view({'get': 'list', 'post': 'create'})),
    path("tasks/code-tasks/<int:code_task>/testcases", TestCaseListView.as_view())
]
