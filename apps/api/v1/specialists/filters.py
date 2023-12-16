from django.db.models import Q
from django_filters import rest_framework as filters

from apps.attributes.crud import list_cities, list_roles, list_jobs
from apps.specialists.models import Specialist


class SpecialistFilterset(filters.FilterSet):
    text = filters.CharFilter(method="find_spec")
    city = filters.ModelMultipleChoiceFilter(queryset=list_cities())
    role = filters.ModelChoiceFilter(queryset=list_roles(), method="find_role")
    job = filters.ModelMultipleChoiceFilter(queryset=list_jobs())

    class Meta:
        model = Specialist
        fields = ("text", "city", "is_colleague", "role", "job")

    def find_spec(self, queryset, name, value):
        """Поиск по вхождению."""
        if value:
            return queryset.filter(
                Q(last_name__icontains=value)
                | Q(email__icontains=value)
                | Q(phone__icontains=value)
                | Q(company__icontains=value)
            )
        return queryset

    def find_role(self, queryset, name, value):
        """Поиск по роли в прошедших мероприятиях."""
        if value:
            return queryset.filter(participants__role=value)
        return queryset
