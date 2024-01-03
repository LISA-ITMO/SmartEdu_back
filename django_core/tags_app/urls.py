from django.urls import path
from .views import TagsListViewSet

urlpatterns = [
    path("tags/", TagsListViewSet.as_view({"get": "list", "post": "create"}))
]