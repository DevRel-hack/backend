from drf_spectacular.utils import extend_schema_view
from rest_framework import views, status
from rest_framework.response import Response

from apps.attributes.crud import get_attributes

from .schema import attrs_schema
from .serializers import AttributesSerializer


@extend_schema_view(**attrs_schema)
class AttributesView(views.APIView):
    """Просмотр всех доступных атрибутов."""

    def get(self, request):
        data = get_attributes()
        serializer = AttributesSerializer(instance=data)
        return Response(serializer.data, status=status.HTTP_200_OK)
