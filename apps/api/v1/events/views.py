from drf_spectacular.utils import extend_schema_view, extend_schema
from rest_framework import viewsets, response, generics

from apps.events.crud import list_events, retrieve_event, list_key_participants

from .schema import (
    events_schema,
    list_participants_schema,
    single_participants_schema,
)
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


@extend_schema(tags=["participants"])
@extend_schema_view(**list_participants_schema)
class ListCreateParticipantView(generics.ListCreateAPIView):
    http_method_names = ["get", "post"]

    def get_queryset(self):
        return list_key_participants(event_id=self.kwargs.get("event_id"))

    def get_serializer_class(self):
        if self.request.method == "POST":
            return ser.CreateParticipantSerializer
        return ser.ParticipantSerializer

    def perform_create(self, serializer):
        event_id = self.kwargs.get("event_id")
        return serializer.save(event_id=event_id)


@extend_schema(tags=["participants"])
@extend_schema_view(**single_participants_schema)
class ParticipantObjView(generics.RetrieveUpdateDestroyAPIView):
    http_method_names = ["get", "patch", "delete"]

    def get_queryset(self):
        return list_key_participants(event_id=self.kwargs.get("event_id"))

    def get_serializer_class(self):
        if self.request.method == "PATCH":
            return ser.EditParticipantSerializer
        return ser.ParticipantSerializer
