from apps.core.models import TitledModel


class City(TitledModel):
    """Модель городов."""

    class Meta:
        verbose_name = "Город"
        verbose_name_plural = "Города"


class Tool(TitledModel):
    """Модель Инструментов и навыков."""

    class Meta:
        verbose_name = "Инструмент"
        verbose_name_plural = "Инструменты"


class Job(TitledModel):
    """Модель направления работы."""

    class Meta:
        verbose_name = "Направление"
        verbose_name_plural = "Направления"


class Tag(TitledModel):
    """Теги."""

    class Meta:
        verbose_name = "Тег"
        verbose_name_plural = "Теги"


class Grade(TitledModel):
    """Уровень развития специалиста."""

    class Meta:
        verbose_name = "Уровень"
        verbose_name_plural = "Уровни"


class EventStatus(TitledModel):
    """Статус проведения мероприятия."""

    class Meta:
        verbose_name = "Статус мероприятия"
        verbose_name_plural = "Статусы мероприятий"


class Role(TitledModel):
    """Роли участников мероприятий."""

    class Meta:
        verbose_name = "Роль участника"
        verbose_name_plural = "Роли участников"
