from rest_framework.generics import ListAPIView
from rest_framework.viewsets import ModelViewSet

from .models import Tag
from .serializers import TagSerializer


class TagsListViewSet(ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer

