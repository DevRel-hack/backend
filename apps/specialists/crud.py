from collections import OrderedDict

from django.db.models import QuerySet, Prefetch

from apps.events.models import Participant

from .models import Specialist


def list_specialists() -> QuerySet[Specialist]:
    return Specialist.objects.select_related(
        "city", "job", "grade"
    ).prefetch_related("tools")


def retrieve_specialist(spec_id: int):
    return (
        Specialist.objects.filter(id=spec_id)
        .select_related("city", "job", "grade")
        .prefetch_related(
            "tools",
            Prefetch(
                "participants",
                queryset=Participant.objects.filter(
                    specialist_id=spec_id
                ).select_related("event", "role"),
            ),
        )
    )


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


def bulk_create_specialists(data: list[dict]) -> None:
    specs = [Specialist(**fields) for fields in data]
    Specialist.objects.bulk_create(specs)
    return None


def bulk_create_spec_tools(data: list[dict]) -> None:
    specs = [Specialist.tools.through(**fields) for fields in data]
    Specialist.tools.through.objects.bulk_create(specs)
    return None


def specialists_are_in_db() -> bool:
    return Specialist.objects.all().exists()
