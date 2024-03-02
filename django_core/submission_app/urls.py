from rest_framework.routers import DefaultRouter
from .views import SubmissionViewSet, UserPromptAPIView
from django.urls import path

urlpatterns = [
    path("giga/", UserPromptAPIView.as_view())
]

router = DefaultRouter()
router.register("submissions", SubmissionViewSet)

urlpatterns += router.urls
