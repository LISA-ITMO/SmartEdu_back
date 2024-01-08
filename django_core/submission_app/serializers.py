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
    output = CharField(read_only=True)

    class Meta:
        model = Submission
        fields = "__all__"


class RetrieveUpdateSubmissionSerializer(ModelSerializer):
    class Meta:
        model = Submission
        fields = ["status"]
