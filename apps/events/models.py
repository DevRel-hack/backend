from django.db import models

from apps.attributes.models import Tag, EventStatus, Role
from apps.core.models import BaseModel
from apps.specialists.models import Specialist


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
        verbose_name = "Мероприятие"
        verbose_name_plural = "Мероприятия"
        default_related_name = "events"

    def __str__(self) -> str:
        return f"{self.title}: {self.start_at}"


class Participant(BaseModel):
    """Модель участника мероприятия."""

    event = models.ForeignKey(
        Event, on_delete=models.CASCADE, verbose_name="Мероприятие"
    )
    specialist = models.ForeignKey(
        Specialist, on_delete=models.CASCADE, verbose_name="Участник"
    )
    role = models.ForeignKey(
        Role, on_delete=models.PROTECT, verbose_name="Роль"
    )
    comment = models.CharField(verbose_name="Комментарии", max_length=255)

    class Meta:
        ordering = ("-event_id", "role_id")
        verbose_name = "Участник"
        verbose_name_plural = "Участники"
        default_related_name = "participants"

    def __str__(self) -> str:
        return f"Участник {self.specialist_id} в мероприятии {self.event_id}"
