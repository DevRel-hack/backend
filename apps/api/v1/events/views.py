from drf_spectacular.utils import extend_schema_view
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action

from apps.events.crud import list_events, list_event_types

from .schema import events_schema, events_types_schema
from .serializers import EventSerializer, EventTypeSerializer


@extend_schema_view(**events_schema)
class EventViewset(viewsets.ModelViewSet):
    """Работа с мероприятиями."""

    queryset = list_events()
    serializer_class = EventSerializer
    http_method_names = ["get", "patch", "post", "delete"]


@extend_schema_view(**events_types_schema)
class EventTypeViewset(viewsets.ReadOnlyModelViewSet):
    """Чтение типов мероприятий."""

    queryset = list_event_types()
    serializer_class = EventTypeSerializer
