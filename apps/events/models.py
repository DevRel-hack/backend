from django.db import models

from apps.attributes.models import Theme
from apps.core.models import BaseModel, TitledModel


class EventType(TitledModel):
    """Модель типа мероприятия."""

    class Meta:
        verbose_name = "Тип мероприятия"
        verbose_name_plural = "Типы мероприятий"


class Event(BaseModel):
    """Модель Мероприятий."""

    class Status(models.TextChoices):
        IDEA = "idea", "Проработка"
        CONC = "conc", "Согласование"
        PREP = "prep", "Подготовка"
        OVER = "over", "Завершено"
        CANCEL = "canc", "Отменено"

    class Format(models.TextChoices):
        ONLINE = "on", "Online"
        OFFLINE = "off", "Offline"
        BOTH = "both", "Online + Offline"

    status = models.CharField(
        verbose_name="Текущий статус", max_length=5, choices=Status.choices
    )
    title = models.CharField(
        verbose_name="Название мероприятия", max_length=200
    )
    start_at = models.DateTimeField(verbose_name="Время и дата начала")
    form = models.CharField(
        verbose_name="Формат", max_length=5, choices=Format.choices
    )
    place = models.CharField(verbose_name="Место проведения", max_length=255)
    type = models.ForeignKey(
        EventType,
        on_delete=models.PROTECT,
        related_name="events",
        verbose_name="Тип мероприятия",
    )
    themes = models.ManyToManyField(Theme, related_name="events")

    class Meta:
        verbose_name = "Тип мероприятия"
        verbose_name_plural = "Типы мероприятий"
