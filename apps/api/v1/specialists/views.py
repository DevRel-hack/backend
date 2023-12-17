from drf_spectacular.utils import extend_schema_view
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action

from apps.specialists.crud import list_specialists, retrieve_specialist
from apps.specialists.services import upload_specialists

from .filters import SpecialistFilterset
from .schema import specialists_schema
from . import serializers as ser


@extend_schema_view(**specialists_schema)
class SpecialistsViewset(viewsets.ModelViewSet):
    """Работа со специалистами."""

    http_method_names = ["get", "patch", "post", "delete"]
    filterset_class = SpecialistFilterset

    def get_serializer_class(self):
        if self.action == "retrieve":
            return ser.RetrieveSpecialistSerializer
        return ser.SpecialistSerializer

    def get_queryset(self):
        if self.action == "retrieve":
            spec_id = self.kwargs.get("pk")
            return retrieve_specialist(spec_id=spec_id)
        return list_specialists()

    @action(methods=["post"], detail=False)
    def upload_fixtures(self, request):
        success = upload_specialists()
        if success:
            return Response(status=status.HTTP_201_CREATED)
        return Response(
            data={"error": "Специалисты уже загружены"},
            status=status.HTTP_400_BAD_REQUEST,
        )
