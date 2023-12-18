from django.urls import path
from .views import (
    TaskListView,
    TaskTypeListView,
    CodeTaskRetrieveView,
    TestCaseListView,
)

urlpatterns = [
    path("tasks", TaskListView.as_view()),
    path("tasks/<int:task>/code-tasks", CodeTaskRetrieveView.as_view()),
    path("tasks/types", TaskTypeListView.as_view()),
    path("tasks/code-tasks/<int:code_task>/testcases", TestCaseListView.as_view()),
]
