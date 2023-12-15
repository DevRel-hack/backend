from collections import OrderedDict

from django.db.models import QuerySet

from .models import Specialist


def list_specialists() -> QuerySet[Specialist]:
    return Specialist.objects.select_related(
        "city", "job", "grade"
    ).prefetch_related("tools")


def specialist_exists(email: str) -> bool:
    return Specialist.objects.filter(email=email).exists()


def create_specialist(data: OrderedDict) -> Specialist:
    return Specialist.objects.create(**data)


def update_specialist(instance: Specialist, data: OrderedDict) -> Specialist:
    for key, value in data.items():
        if getattr(instance, key):
            setattr(instance, key, value)
    instance.save()
    return instance
