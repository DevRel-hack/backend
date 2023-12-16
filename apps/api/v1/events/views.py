from drf_spectacular.utils import extend_schema, extend_schema_view
from rest_framework import generics, views, viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from apps.events.crud import list_events, list_key_participants, retrieve_event
from apps.events.services import upload_events

from . import serializers as ser
from .filters import EventFilterset
from .schema import (
    events_schema,
    list_participants_schema,
    single_participants_schema,
)


@extend_schema_view(**events_schema)
class EventViewset(viewsets.ModelViewSet):
    """Работа с мероприятиями."""

    http_method_names = ["get", "patch", "post", "delete"]
    filterset_class = EventFilterset

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


class UploadEventsView(views.APIView):
    def post(self, request):
        success = upload_events()
        if success:
            return Response(status=status.HTTP_201_CREATED)
        return Response(
            data={"error": "Мероприятия уже загружены"},
            status=status.HTTP_400_BAD_REQUEST,
        )


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
