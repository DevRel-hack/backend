from drf_spectacular.utils import extend_schema_view
from rest_framework import viewsets

from apps.events.crud import list_events

from .schema import events_schema
from .serializers import EventSerializer


@extend_schema_view(**events_schema)
class EventViewset(viewsets.ModelViewSet):
    """Работа с мероприятиями."""

    queryset = list_events()
    serializer_class = EventSerializer
    http_method_names = ["get", "patch", "post", "delete"]
