from rest_framework.views import APIView
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import CreateModelMixin, RetrieveModelMixin
from .models import Submission, UserPrompt
from .serializers import (
    CreateSubmissionSerializer,
    RetrieveUpdateSubmissionSerializer,
    UserPromptSerializer
)
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .utils.prompt_builders import PromptBuilder, get_code_form_submission
from .utils.gigachat_adapter import GigaChatAdapter
from .tasks import send_prompt_by_submission
from celery.result import AsyncResult


class SubmissionViewSet(
    GenericViewSet, CreateModelMixin, RetrieveModelMixin
):

    """
    POST: Creates `Submission` and send code to "Code checker" \n
    GET: Returns status of testing \n
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


class UserPromptAPIView(APIView):

    def post(self, submission_pk):
        submission_pk = send_prompt_by_submission.delay(submission_pk)

        # prompt = PromptBuilder(get_code_form_submission(submission_pk))
        # answer = GigaChatAdapter()
        return Response(status=201,data=submission_pk.id)

    def get(self, task_id):
        result = AsyncResult(id=task_id)
#         проверить таск-id
        if result.status == "SUCCESS":
            return Response(status=200, data={"status":result.status, 'data':result.result })
        return Response(status=200, data={"status":result.status, 'data':None})




