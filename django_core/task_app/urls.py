from django.urls import path, include
from rest_framework import routers

from .views import (
    CodeTaskRetrieveView,
    TestCaseListView,
    TaskListViewSet,
    TaskTypeListView,
)

router = routers.DefaultRouter()
router.register(r'tasks', TaskListViewSet)


urlpatterns = [
    path("", include(router.urls)),
    path("tasks/<int:task>/code-tasks", CodeTaskRetrieveView.as_view()),
    path("tasks/types", TaskTypeListView.as_view()),
    path("tasks/code-tasks/<int:code_task>/testcases", TestCaseListView.as_view())
]
