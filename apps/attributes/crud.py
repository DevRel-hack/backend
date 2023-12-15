from django.db.models import QuerySet

from .models import City, Tool, Job, Grade, Theme


def list_cities() -> QuerySet[City]:
    return City.objects.all()


def list_tools() -> QuerySet[Tool]:
    return Tool.objects.all()


def list_jobs() -> QuerySet[Job]:
    return Job.objects.all()


def list_grades() -> QuerySet[Grade]:
    return Grade.objects.all()


def list_themes() -> QuerySet[Theme]:
    return Theme.objects.all()


def get_attributes() -> dict[str, QuerySet]:
    return {
        "cities": list_cities(),
        "tools": list_tools(),
        "jobs": list_jobs(),
        "grades": list_grades(),
        "themes": list_themes(),
    }
