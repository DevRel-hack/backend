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


class Theme(TitledModel):
    """Темы."""

    class Meta:
        verbose_name = "Направление"
        verbose_name_plural = "Направления"


class Grade(TitledModel):
    """Уровень развития специалиста."""

    class Meta:
        verbose_name = "Уровень"
        verbose_name_plural = "Уровни"
