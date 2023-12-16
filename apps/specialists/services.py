from collections import OrderedDict

from django.db.transaction import atomic

from apps.core.utils import get_spec_tools_datasets, get_specialists_datasets

from .crud import (
    bulk_create_spec_tools,
    bulk_create_specialists,
    create_specialist,
    specialists_are_in_db,
    update_specialist,
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


@atomic
def upload_specialists() -> None:
    if not specialists_are_in_db():
        spec_dataset = get_specialists_datasets()
        bulk_create_specialists(data=spec_dataset)
        spec_tools_datasets = get_spec_tools_datasets()
        bulk_create_spec_tools(data=spec_tools_datasets)
        return True
    return False
