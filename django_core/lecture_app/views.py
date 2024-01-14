from rest_framework.generics import ListAPIView
from rest_framework.viewsets import ModelViewSet

from .models import (
    Theory,
    TheoryType,
    TheoryPresentContent,
    TheoryVideoContent,
    TheoryTextContent,
)
from .serializers import (
    TheorySerializer,
    TheoryTypeSerializer,
    TheoryPresentContentSerializer,
    TheoryVideoContentSerializer,
    TheoryTextContentSerializer,
)
from .paginations import TheoryPagination
from django_filters.rest_framework import DjangoFilterBackend
from .filters import TheoryFilter


class TheoryListViewSet(ModelViewSet):
    """
        Returns list of existing Theories.
        provides pagination and filter by `theory_type`.
        Also provide filter by `tags`
        """
    queryset = Theory.objects.all()
    serializer_class = TheorySerializer
    pagination_class = TheoryPagination

    filter_backends = [DjangoFilterBackend]
    filterset_class = TheoryFilter


class TheoryTypeListView(ListAPIView):
    """
    Returns list of all `TheoryType`'s
    """

    queryset = TheoryType.objects.all()
    serializer_class = TheoryTypeSerializer


class TheoryPresentContentListView(ListAPIView):
    """
    Return files by `Theory` `id`
    """

    queryset = TheoryPresentContent.objects.all()
    serializer_class = TheoryPresentContentSerializer
    lookup_field = "theory"


class TheoryVideoContentListView(ListAPIView):
    """
    Return video content by theory `id`
    """

    queryset = TheoryVideoContent.objects.all()
    serializer_class = TheoryVideoContentSerializer
    lookup_field = "theory"


class TheoryTextContentListView(ListAPIView):
    """
    Return text content by theory `id`
    """

    queryset = TheoryTextContent.objects.all()
    serializer_class = TheoryTextContentSerializer
    lookup_field = "theory"
