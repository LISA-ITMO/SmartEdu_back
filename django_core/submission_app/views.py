from rest_framework.generics import CreateAPIView, RetrieveAPIView
from .models import Submission
from .serializers import CreateSubmissionSerializer, RetrieveSubmissionSerializer
from rest_framework.permissions import IsAuthenticated


class SubmissionCreateView(CreateAPIView):
    """
    Creates and send to "Code checker" code snippet
    """

    permission_classes = [IsAuthenticated]
    queryset = Submission.objects.all()
    serializer_class = CreateSubmissionSerializer


class SubmissionRetrieveView(RetrieveAPIView):
    """
    Returns status of testing `Task`
    """

    permission_classes = [IsAuthenticated]
    serializer_class = RetrieveSubmissionSerializer
    queryset = Submission.objects.all()
