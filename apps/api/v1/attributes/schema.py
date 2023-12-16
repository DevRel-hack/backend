from drf_spectacular.utils import extend_schema, OpenApiParameter

from .serializers import AttributesSerializer, StatisticsSerializer


attrs_schema = {
    "get": extend_schema(
        summary="Список атрибутов", responses={200: AttributesSerializer}
    )
}


stats_schema = {
    "get": extend_schema(
        summary="Статистика по атрибутам",
        responses={200: StatisticsSerializer},
        parameters=[
            OpenApiParameter(
                name="event_id",
                type=int,
                description="Фильтр по мероприятию",
            ),
        ],
    )
}
