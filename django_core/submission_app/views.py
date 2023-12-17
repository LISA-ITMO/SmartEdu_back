from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import CreateModelMixin, RetrieveModelMixin, UpdateModelMixin
from .models import Submission
from .serializers import (
    CreateSubmissionSerializer,
    RetrieveUpdateSubmissionSerializer
)
from rest_framework.permissions import IsAuthenticated


class SubmissionViewSet(
    GenericViewSet, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin
):

    """
    POST: Creates `Submission` and send code to "Code checker" \n
    GET: Returns status of testing \n
    PUT and PATCH: For internal usage only! (Access by API-KEY)
    """

    permission_classes = {
        "GET": [IsAuthenticated],
        "POST": [IsAuthenticated],
        "PUT": [],
    }

    queryset = Submission.objects.all()

    def get_serializer_class(self):
        match self.request.method:
            case "GET":
                return RetrieveUpdateSubmissionSerializer

            case "POST":
                return CreateSubmissionSerializer

            case _:
                return RetrieveUpdateSubmissionSerializer

    def get_permissions(self):
        method = self.request.method
        return [permission() for permission in self.permission_classes.get(method, [])]
