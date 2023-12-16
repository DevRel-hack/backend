from drf_spectacular.utils import extend_schema_view
from rest_framework import views, status
from rest_framework.response import Response

from apps.attributes.crud import get_attributes, get_statistics

from .schema import attrs_schema, stats_schema
from . import serializers as ser


@extend_schema_view(**attrs_schema)
class AttributesView(views.APIView):
    """Просмотр всех доступных атрибутов."""

    def get(self, request):
        data = get_attributes()
        serializer = ser.AttributesSerializer(instance=data)
        return Response(serializer.data, status=status.HTTP_200_OK)


@extend_schema_view(**stats_schema)
class StatisticsView(views.APIView):
    def get(self, request):
        event_id = self.request.query_params.get("event_id")
        data = get_statistics(event_id=event_id)
        serializer = ser.StatisticsSerializer(instance=data)
        return Response(serializer.data, status=status.HTTP_200_OK)
