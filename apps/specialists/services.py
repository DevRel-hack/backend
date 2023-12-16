from collections import OrderedDict

from apps.core.utils import get_specialists_datasets

from .crud import (
    create_specialist,
    update_specialist,
    bulk_create_specialists,
    specialists_are_in_db,
)
from .models import Specialist


def add_specialist(data: OrderedDict) -> Specialist:
    tools = data.pop("tools")
    specialist = create_specialist(data=data)
    specialist.tools.set(tools)
    return specialist


def edit_specialist(instance: Specialist, data: OrderedDict) -> Specialist:
    tools = data.pop("tools")
    specialist = update_specialist(instance, data)
    specialist.tools.clear()
    specialist.tools.set(tools)
    return specialist


def upload_specialists() -> None:
    if not specialists_are_in_db():
        dataset = get_specialists_datasets()
        bulk_create_specialists(data=dataset)
        return True
    return False
