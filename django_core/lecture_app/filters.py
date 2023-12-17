from django_filters.rest_framework import BaseInFilter, CharFilter, FilterSet

from .models import Theory


class CharFilterInFilter(BaseInFilter, CharFilter):
    pass


class TheoryFilter(FilterSet):

    class Meta:
        model = Theory
        fields = ["theory_type", "tags"]
