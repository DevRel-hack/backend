from collections import OrderedDict

from django.db.transaction import atomic

from apps.core.utils import (
    get_event_tags_datasets,
    get_events_datasets,
    get_participants_datasets,
)
from apps.specialists.crud import specialists_are_in_db

from .crud import (
    bulk_create_event_tags,
    bulk_create_events,
    bulk_create_participants,
    create_event,
    events_in_db,
    update_event,
)
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


@atomic
def upload_events() -> None:
    if not events_in_db() and specialists_are_in_db():
        events_dataset = get_events_datasets()
        bulk_create_events(dataset=events_dataset)
        events_tags_datasets = get_event_tags_datasets()
        bulk_create_event_tags(data=events_tags_datasets)
        participants_datasets = get_participants_datasets()
        bulk_create_participants(data=participants_datasets)
        return True
    return False
