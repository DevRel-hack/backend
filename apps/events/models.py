from django.db import models

from apps.attributes.models import Tag, EventStatus
from apps.core.models import BaseModel


# class EventType(TitledModel):
#     """Модель типа мероприятия."""

#     class Meta:
#         verbose_name = "Тип мероприятия"
#         verbose_name_plural = "Типы мероприятий"


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

    status = models.ForeignKey(
        EventStatus, on_delete=models.PROTECT, verbose_name="Статус"
    )
    title = models.CharField(
        verbose_name="Название мероприятия", max_length=200
    )
    description = models.TextField(
        verbose_name="Описание", max_length=5000, blank=True
    )
    start_at = models.DateTimeField(verbose_name="Время и дата начала")
    is_internal = models.BooleanField(verbose_name="Мероприятие внутреннее")
    form = models.CharField(
        verbose_name="Формат", max_length=5, choices=Format.choices
    )
    place = models.CharField(
        verbose_name="Место проведения", max_length=255, blank=True
    )
    tags = models.ManyToManyField(Tag, verbose_name="Теги", blank=True)
    url = models.URLField(
        verbose_name="Ссылка на страницу мероприятия", blank=True
    )
    comments = models.TextField(verbose_name="Комментарии", blank=True)

    class Meta:
        verbose_name = "Тип мероприятия"
        verbose_name_plural = "Типы мероприятий"
        default_related_name = "events"

    def __str__(self) -> str:
        return f"{self.title}: {self.start_at}"
