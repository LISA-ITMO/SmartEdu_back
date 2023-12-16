from rest_framework.generics import ListAPIView
from .models import Theory
from .serializers import TheorySerializer
from .paginations import TheoryPagination
from django_filters.rest_framework import DjangoFilterBackend
from .filters import TheoryFilter


class TheoryListView(ListAPIView):
    """
    Returns list of existing Theories.
    provides pagination and filter by `theory_type`.
    """

    queryset = Theory.objects.all()
    serializer_class = TheorySerializer
    pagination_class = TheoryPagination

    filter_backends = [DjangoFilterBackend]
    filterset_class = TheoryFilter
