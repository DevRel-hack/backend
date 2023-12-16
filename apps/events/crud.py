from collections import OrderedDict

from django.db.models import QuerySet, Prefetch

from .models import Event, Participant


def list_events() -> QuerySet[Event]:
    return Event.objects.select_related("status").prefetch_related("tags")


def retrieve_event(event_id: int) -> Event:
    # исправить запросы
    return Event.objects.filter(id=event_id).prefetch_related(
        Prefetch(
            "participants",
            queryset=Participant.objects.filter(event_id=event_id)
            .exclude(role_id=1)
            .select_related("specialist", "role"),
        )
    )


def create_event(data: OrderedDict) -> Event:
    return Event.objects.create(**data)


def update_event(event: Event, data: OrderedDict) -> Event:
    for key, value in data.items():
        if getattr(event, key):
            setattr(event, key, value)
    event.save()
    return event


def list_key_participants(event_id: int) -> QuerySet[Participant]:
    return (
        Participant.objects.filter(event_id=event_id)
        .exclude(role_id=1)
        .select_related("specialist", "role")
    )


def events_in_db() -> bool:
    return Event.objects.exists()


def bulk_create_events(dataset: list[dict]) -> None:
    events = [Event(**fields) for fields in dataset]
    Event.objects.bulk_create(events)


def bulk_create_event_tags(data: list[dict]) -> None:
    connection = [Event.tags.through(**fields) for fields in data]
    Event.tags.through.objects.bulk_create(connection)
    return None


def bulk_create_participants(data: list[dict]) -> None:
    parts = [Participant(**fields) for fields in data]
    Participant.objects.bulk_create(parts)
    return None
