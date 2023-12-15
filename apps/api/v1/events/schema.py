from drf_spectacular.utils import extend_schema


events_schema = {
    "list": extend_schema(summary="Список мероприятий"),
    "retrieve": extend_schema(summary="Просмотр мероприятия по ID"),
    "create": extend_schema(summary="Добавление нового мероприятия"),
    "partial_update": extend_schema(summary="Изменение мероприятия"),
    "destroy": extend_schema(summary="Удаление мероприятия"),
}


events_types_schema = {
    "list": extend_schema(summary="Список типов мероприятий"),
    "retrieve": extend_schema(summary="Просмотр типа мероприятия по ID"),
}
