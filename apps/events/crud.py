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


# def list_key_participants() -> QuerySet[Participant]:
#     a = (
#         Participant.objects.all()
#         .exclude(role_id=1)
#         .select_related("specialist", "role")
#     )
#     return a
