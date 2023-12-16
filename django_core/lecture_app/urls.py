from django.urls import path

from .views import TheoryListView

urlpatterns = [
    path("theory/", TheoryListView.as_view()),
]