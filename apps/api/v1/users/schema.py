from drf_spectacular.utils import extend_schema


users_schema = {
    "create": extend_schema(
        summary="Создание пользователя",
        description="Создание нового пользователя.",
    ),
    "list": extend_schema(
        summary="Список пользователей",
        description="Получение списка пользователей.",
    ),
    "retrieve": extend_schema(
        summary="Данные о пользователе по ID",
        description="Получение данных пользователя.",
    ),
    "update": extend_schema(exclude=True),
    "partial_update": extend_schema(exclude=True),
    "destroy": extend_schema(exclude=True),
    "reset_username": extend_schema(exclude=True),
    "set_username": extend_schema(exclude=True),
    "reset_username_confirm": extend_schema(exclude=True),
    "resend_activation": extend_schema(exclude=True),
    "activation": extend_schema(exclude=True),
    "me": extend_schema(
        summary="Текущий пользователь",
        description="Данные о текущем пользователе.",
    ),
    "reset_password": extend_schema(exclude=True),
    "reset_password_confirm": extend_schema(exclude=True),
    "set_password": extend_schema(exclude=True),
}
