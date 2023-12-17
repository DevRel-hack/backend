from drf_spectacular.utils import extend_schema, OpenApiParameter


specialists_schema = {
    "list": extend_schema(
        summary="Список специалистов",
        parameters=[
            OpenApiParameter(
                name="city",
                type=list[int],
                description="Мультивыбор городов по имени",
            ),
            OpenApiParameter(
                name="text",
                description="Поиск по фамилии/email/телефону/компании",
            ),
            OpenApiParameter(
                name="is_colleague",
                type=bool,
                description="Является сотрудником компании",
            ),
            OpenApiParameter(
                name="job",
                type=list[int],
                description="Направление работы",
            ),
            OpenApiParameter(
                name="role",
                type=int,
                description="Роль в прошедших мероприятиях",
            ),
        ],
    ),
    "retrieve": extend_schema(summary="Просмотр специалиста по ID"),
    "create": extend_schema(summary="Добавление нового специалиста"),
    "partial_update": extend_schema(summary="Изменение специалиста"),
    "destroy": extend_schema(summary="Удаление специалиста"),
    "upload_fixtures": extend_schema(summary="Загрузка фикстур специалистов"),
}
