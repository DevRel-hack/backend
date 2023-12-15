from collections import OrderedDict

from django.db.models import QuerySet

from .models import Event, EventType


def list_events() -> QuerySet[Event]:
    return Event.objects.select_related("type").prefetch_related("themes")


def list_event_types() -> QuerySet[EventType]:
    return EventType.objects.all()


def create_event(data: OrderedDict) -> Event:
    return Event.objects.create(**data)


def update_event(event: Event, data: OrderedDict) -> Event:
    for key, value in data.items():
        if getattr(event, key):
            setattr(event, key, value)
    event.save()
    return event
