from drf_spectacular.utils import extend_schema, OpenApiExample


request_sample = {
    "status": 1,
    "title": "Новый Хакатон",
    "description": "Много слов о мероприятии",
    "start_at": "16.12.2023 18:00",
    "is_internal": False,
    "form": "on",
    "place": "интернет",
    "url": "https://linktoevent.com",
    "type": 1,
    "tags": [1, 2, 3],
    "comments": "Комментарии",
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
                value=request_sample,
                request_only=True,
            ),
        ],
    ),
    "partial_update": extend_schema(summary="Изменение мероприятия"),
    "destroy": extend_schema(summary="Удаление мероприятия"),
}
