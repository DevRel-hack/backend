from collections import OrderedDict

from .crud import create_specialist, update_specialist
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
