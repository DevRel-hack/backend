from drf_spectacular.utils import extend_schema_view
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action

from apps.specialists.crud import list_specialists

from .schema import specialists_schema
from .serializers import SpecialistSerializer


@extend_schema_view(**specialists_schema)
class SpecialistsViewset(viewsets.ModelViewSet):
    """Работа со специалистами."""

    queryset = list_specialists()
    serializer_class = SpecialistSerializer
    http_method_names = ["get", "patch", "post", "delete"]
