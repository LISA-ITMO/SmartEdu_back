from django.urls import path
from .views import SubmissionCreateView, SubmissionRetrieveView

urlpatterns = [
    path("submission", SubmissionCreateView.as_view()),
    path("submission/<int:pk>", SubmissionRetrieveView.as_view()),
]
