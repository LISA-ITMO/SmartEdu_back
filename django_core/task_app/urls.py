from django.urls import path
from .views import (
    TaskListView,
    TaskTypeListView,
    CodeTaskRetrieveView,
    TestCaseListView,
)

urlpatterns = [
    path("tasks", TaskListView.as_view()),
    path("tasks/<int:task>", CodeTaskRetrieveView.as_view()),
    path("tasks/types", TaskTypeListView.as_view()),
    path("tasks/<int:task>/testcases", TestCaseListView.as_view()),
]
