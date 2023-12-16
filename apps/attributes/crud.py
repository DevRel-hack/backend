from django.db.models import QuerySet

from .models import City, Tool, Job, Grade, Tag, EventStatus, Role


def list_cities() -> QuerySet[City]:
    return City.objects.all()


def list_tools() -> QuerySet[Tool]:
    return Tool.objects.all()


def list_jobs() -> QuerySet[Job]:
    return Job.objects.all()


def list_grades() -> QuerySet[Grade]:
    return Grade.objects.all()


def list_tags() -> QuerySet[Tag]:
    return Tag.objects.all()


def list_roles() -> QuerySet[Role]:
    return Role.objects.all()


def list_statuses() -> QuerySet[EventStatus]:
    return EventStatus.objects.all()


def get_attributes() -> dict[str, QuerySet]:
    return {
        "cities": list_cities(),
        "tools": list_tools(),
        "jobs": list_jobs(),
        "grades": list_grades(),
        "tags": list_tags(),
        "roles": list_roles(),
        "statuses": list_statuses(),
    }
