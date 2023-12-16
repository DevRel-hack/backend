from drf_spectacular.utils import extend_schema_view
from rest_framework import viewsets

from apps.events.crud import list_events, retrieve_event

from .schema import events_schema
from . import serializers as ser


@extend_schema_view(**events_schema)
class EventViewset(viewsets.ModelViewSet):
    """Работа с мероприятиями."""

    http_method_names = ["get", "patch", "post", "delete"]

    def get_serializer_class(self):
        if self.action == "list":
            return ser.ListEventSerializer
        if self.action == "retrieve":
            return ser.RetrieveEventSerializer
        return ser.CreateEditEventSerializer

    def get_queryset(self):
        if self.action == "retrieve":
            event_id = self.kwargs.get("pk")
            return retrieve_event(event_id=event_id)
        return list_events()
