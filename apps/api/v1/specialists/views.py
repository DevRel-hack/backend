from drf_spectacular.utils import extend_schema_view
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action

from apps.specialists.crud import list_specialists
from apps.specialists.services import upload_specialists

from .filters import SpecialistFilterset
from .schema import specialists_schema
from .serializers import SpecialistSerializer


@extend_schema_view(**specialists_schema)
class SpecialistsViewset(viewsets.ModelViewSet):
    """Работа со специалистами."""

    queryset = list_specialists()
    serializer_class = SpecialistSerializer
    http_method_names = ["get", "patch", "post", "delete"]
    filterset_class = SpecialistFilterset

    @action(methods=["post"], detail=False)
    def upload_specialists(self, request):
        success = upload_specialists()
        if success:
            return Response(status=status.HTTP_201_CREATED)
        return Response(
            data={"error": "Специалисты уже загружены"},
            status=status.HTTP_400_BAD_REQUEST,
        )
