from collections import OrderedDict

from django.db.models import QuerySet, Subquery, OuterRef

from .models import Event, Participant


def list_events() -> QuerySet[Event]:
    return Event.objects.select_related("status").prefetch_related("tags")


def retrieve_event(event_id: int) -> Event:
    return Event.objects.filter(id=event_id).annotate(
        key_parts=Subquery(
            Participant.objects.filter(event_id=OuterRef("pk")).select_related(
                "specialist", "role"
            )
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
