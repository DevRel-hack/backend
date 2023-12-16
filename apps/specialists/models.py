from django.db import models

from apps.attributes.models import City, Job, Grade, Tool
from apps.core.models import BaseModel


class Specialist(BaseModel):
    """Модель специалиста."""

    first_name = models.CharField(
        verbose_name="Имя", max_length=50, blank=True
    )
    last_name = models.CharField(
        verbose_name="Фамилия", max_length=50, blank=True
    )
    phone = models.CharField(
        verbose_name="Номер телефона",
        max_length=15,
        null=True,
    )
    email = models.EmailField(verbose_name="E-mail", unique=True)
    company = models.CharField(
        verbose_name="Компания", max_length=60, blank=True
    )
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
        blank=True,
        verbose_name="Инструменты",
    )

    class Meta:
        verbose_name = "Специалист"
        verbose_name_plural = "Специалисты"
        default_related_name = "specialists"

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"
