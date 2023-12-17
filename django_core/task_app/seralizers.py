from rest_framework.serializers import ModelSerializer
from .models import Task, CodeTask, TaskType, TestCase


class TaskSerializer(ModelSerializer):
    class Meta:
        model = Task
        fields = ("id", "name", "difficulty", "description", "type", "tags")


class TaskTypeSerializer(ModelSerializer):
    class Meta:
        model = TaskType
        fields = "__all__"


class CodeTaskSerializer(ModelSerializer):
    class Meta:
        model = CodeTask
        fields = "__all__"


class TestCaseSerializer(ModelSerializer):
    class Meta:
        model = TestCase
        fields = "__all__"
