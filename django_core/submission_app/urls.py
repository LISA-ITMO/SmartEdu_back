from rest_framework.routers import DefaultRouter
from .views import SubmissionViewSet

urlpatterns = []

router = DefaultRouter()
router.register("submissions", SubmissionViewSet)

urlpatterns += router.urls
