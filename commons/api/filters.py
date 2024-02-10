from django_filters.rest_framework import CharFilter, FilterSet
from rest_framework.filters import BaseFilterBackend


class IsOwnerFilterBackend(BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        return queryset.filter(user=view.user)


class NameContainsFilter(FilterSet):
    name = CharFilter(lookup_expr="name__icontains")
