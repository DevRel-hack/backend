from django.db.models import Q
from django_filters import rest_framework as filters

from apps.attributes.crud import list_tags, list_statuses
from apps.events.models import Event


class EventFilterset(filters.FilterSet):
    title = filters.CharFilter(lookup_expr="icontains")
    tag = filters.ModelMultipleChoiceFilter(queryset=list_tags())
    status = filters.ModelMultipleChoiceFilter(queryset=list_statuses())

    class Meta:
        model = Event
        fields = ("title", "tag", "status")
