from django.urls import path
from rest_framework import routers

from .views import (TheoryListViewSet,
                    TheoryTypeListView,
                    TheoryPresentContentListViewSet,
                    TheoryVideoContentListViewSet,
                    TheoryTextContentListViewSet)

router = routers.DefaultRouter()
router.register(r'theory', TheoryListViewSet)
router.register(r'theory/(\d+)/files', TheoryPresentContentListViewSet)
router.register(r'theory/(\d+)/texts', TheoryTextContentListViewSet)
router.register(r'theory/(\d+)/videos', TheoryVideoContentListViewSet)

router = routers.DefaultRouter()
router.register(r'theory', TheoryListViewSet)

urlpatterns = [
    path("theory/types", TheoryTypeListView.as_view()),
    path("theory/<int:theory>/files", TheoryPresentContentListView.as_view()),
    path("theory/<int:theory>/texts", TheoryTextContentListView.as_view()),
    path("theory/<int:theory>/videos", TheoryVideoContentListView.as_view())
]

urlpatterns += router.urls
