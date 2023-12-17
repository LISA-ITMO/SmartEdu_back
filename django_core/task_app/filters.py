from django_filters.rest_framework import FilterSet
from .models import Task


class TaskFilterSet(FilterSet):
    class Meta:
        model = Task
        fields = ["type", "tags"]
