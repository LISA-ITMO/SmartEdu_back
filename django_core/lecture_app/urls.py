from django.urls import path
from rest_framework import routers

from .views import (TheoryListViewSet,
                    TheoryTypeListView,
                    TheoryPresentContentListView,
                    TheoryVideoContentListView,
                    TheoryTextContentListView)

router = routers.DefaultRouter()
router.register(r'theory', TheoryListViewSet)

urlpatterns = [
    path("theory/types", TheoryTypeListView.as_view()),
    path("theory/<int:theory>/files", TheoryPresentContentListView.as_view()),
    path("theory/<int:theory>/texts", TheoryTextContentListView.as_view()),
    path("theory/<int:theory>/videos", TheoryVideoContentListView.as_view())
]
urlpatterns += router.urls
