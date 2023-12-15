from drf_spectacular.utils import extend_schema


specialists_schema = {
    "list": extend_schema(summary="Список специалистов"),
    "retrieve": extend_schema(summary="Просмотр специалиста по ID"),
    "create": extend_schema(summary="Добавление нового специалиста"),
    "partial_update": extend_schema(summary="Изменение специалиста"),
    "destroy": extend_schema(summary="Удаление специалиста"),
    "upload_specialists": extend_schema(
        summary="Загрузка участников мероприятия", responses={201: None}
    ),
}
