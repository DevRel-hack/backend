from collections import OrderedDict

from django.db.models import QuerySet

from .models import Event


def list_events() -> QuerySet[Event]:
    return Event.objects.select_related("status").prefetch_related("tags")


def create_event(data: OrderedDict) -> Event:
    return Event.objects.create(**data)


def update_event(event: Event, data: OrderedDict) -> Event:
    for key, value in data.items():
        if getattr(event, key):
            setattr(event, key, value)
    event.save()
    return event
