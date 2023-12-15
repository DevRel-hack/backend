from django.db import models

from apps.attributes.models import City, Job, Grade, Tool
from apps.core.models import BaseModel


class Specialist(BaseModel):
    """Модель специалиста."""

    phone = models.CharField(
        verbose_name="Номер телефона",
        max_length=15,
        null=True,
    )
    email = models.EmailField(verbose_name="E-mail", unique=True)
    is_colleague = models.BooleanField(verbose_name="Сотрудник компании")
    city = models.ForeignKey(
        City,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        verbose_name="Город",
    )
    job = models.ForeignKey(
        Job, on_delete=models.PROTECT, verbose_name="Должность"
    )
    grade = models.ForeignKey(
        Grade,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        verbose_name="Должность",
    )
    tools = models.ManyToManyField(
        Tool,
        related_name="specialists",
        blank=True,
        verbose_name="Инструменты",
    )
