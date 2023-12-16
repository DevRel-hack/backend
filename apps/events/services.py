from collections import OrderedDict

from .crud import create_event, update_event
from .models import Event


def add_event(data: OrderedDict) -> Event:
    tags = data.pop("tags")
    event = create_event(data=data)
    event.tags.set(tags)
    return event


def edit_event(instance: Event, data: OrderedDict) -> Event:
    tags = data.pop("tags")
    event = update_event(event=instance, data=data)
    event.tags.clear()
    event.tags.set(tags)
    return event
