from django.urls import path

from .views import (TheoryListView,
                    TheoryTypeListView,
                    TheoryPresentContentListView,
                    TheoryVideoContentListView,
                    TheoryTextContentListView)

urlpatterns = [
    path("theory/", TheoryListView.as_view()),
    path("theory/types", TheoryTypeListView.as_view()),
    path("theory/<int:theory>/files", TheoryPresentContentListView.as_view()),
    path("theory/<int:theory>/texts", TheoryTextContentListView.as_view()),
    path("theory/<int:theory>/videos", TheoryVideoContentListView.as_view())
]