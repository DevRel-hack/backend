from collections import OrderedDict

from .crud import create_event, update_event
from .models import Event


def add_event(data: OrderedDict) -> Event:
    themes = data.pop("themes")
    event = create_event(data=data)
    event.themes.set(themes)
    return event


def edit_event(instance: Event, data: OrderedDict) -> Event:
    themes = data.pop("themes")
    event = update_event(event=instance, data=data)
    event.tools.clear()
    event.tools.set(themes)
    return event
