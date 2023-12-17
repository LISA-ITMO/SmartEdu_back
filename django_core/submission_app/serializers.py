from rest_framework.serializers import (
    ModelSerializer,
    HiddenField,
    CurrentUserDefault,
    CharField,
)
from .models import Submission


class CreateSubmissionSerializer(ModelSerializer):
    user = HiddenField(default=CurrentUserDefault())
    status = CharField(read_only=True)
    worker_uuid = CharField(read_only=True)

    class Meta:
        model = Submission
        fields = "__all__"


class RetrieveSubmissionSerializer(ModelSerializer):
    class Meta:
        model = Submission
        fields = ["status"]
