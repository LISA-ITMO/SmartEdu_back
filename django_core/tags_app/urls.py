from django.urls import path
from .views import TagsListView

urlpatterns = [
    path("tags/", TagsListView.as_view())
]