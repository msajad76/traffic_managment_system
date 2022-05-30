from django_filters.rest_framework import FilterSet, filters
from .models import Vehicle


class VehicleFilter(FilterSet):
    min_age = filters.NumberFilter(field_name='owner__age', lookup_expr='gt')
    color = filters.BaseInFilter(method='color_filter')

    class Meta:
        model = Vehicle
        fields = []

    def color_filter(self, queryset, name, value):
        lookup = f"({'|'.join(value)})"
        return queryset.filter(color__iregex=lookup)
