from drf_spectacular.utils import extend_schema, OpenApiExample


response_sample = {
    "status": "idea",
    "title": "Новый Хакатон",
    "start_at": "16.12.2023 18:00",
    "form": "on",
    "place": "string",
    "type": 1,
    "themes": [1, 2, 3],
}

events_schema = {
    "list": extend_schema(summary="Список мероприятий"),
    "retrieve": extend_schema(summary="Просмотр мероприятия по ID"),
    "create": extend_schema(
        summary="Добавление нового мероприятия",
        examples=[
            OpenApiExample(
                "Valid example 1",
                summary="short summary",
                description="longer description",
                value=[response_sample],
                response_only=True,
            ),
        ],
    ),
    "partial_update": extend_schema(summary="Изменение мероприятия"),
    "destroy": extend_schema(summary="Удаление мероприятия"),
}


events_types_schema = {
    "list": extend_schema(summary="Список типов мероприятий"),
    "retrieve": extend_schema(summary="Просмотр типа мероприятия по ID"),
}
