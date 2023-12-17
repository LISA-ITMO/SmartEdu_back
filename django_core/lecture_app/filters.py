from django_filters.rest_framework import BaseInFilter, CharFilter, FilterSet

from .models import Theory


class CharFilterInFilter(BaseInFilter, CharFilter):
    pass


class TheoryFilter(FilterSet):
    theory_type = CharFilterInFilter(field_name="theory_type__title", lookup_expr="in")

    class Meta:
        model = Theory
        fields = ["theory_type"]
