from django.db.models import QuerySet, Count, Q

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


def stat_tags(event_id: int | None = None) -> QuerySet[Tag]:
    """Статистика по тегам."""
    tags = Tag.objects.all()
    if event_id is None:
        return tags.annotate(
            visitors=Count("events__participants", distinct=True)
        )
    return tags.annotate(
        visitors=Count(
            "events__participants",
            distinct=True,
            filter=Q(events__id=event_id),
        )
    )


def stat_jobs(event_id: int | None = None) -> QuerySet[Job]:
    """Статистика по направлениям работы."""
    jobs = Job.objects.all()
    if event_id is None:
        return jobs.annotate(
            visitors=Count("specialists__participants", distinct=True)
        )
    return jobs.annotate(
        visitors=Count(
            "specialists__participants",
            distinct=True,
            filter=Q(specialists__participants__event_id=event_id),
        )
    )


def stat_grade(event_id: int | None = None) -> QuerySet[Grade]:
    """Статистика по уровню сециалистов."""
    grades = Grade.objects.all()
    if event_id is None:
        return grades.annotate(
            visitors=Count("specialists__participants", distinct=True)
        )
    return grades.annotate(
        visitors=Count(
            "specialists__participants",
            distinct=True,
            filter=Q(specialists__participants__event_id=event_id),
        )
    )


def stat_tools(event_id: int | None = None) -> QuerySet[Tool]:
    """Статистика по инструментам."""
    tools = Tool.objects.all()
    if event_id is None:
        return tools.annotate(
            visitors=Count("specialists__participants", distinct=True)
        )
    return tools.annotate(
        visitors=Count(
            "specialists__participants",
            distinct=True,
            filter=Q(specialists__participants__event_id=event_id),
        )
    )


def get_statistics(event_id: int | None = None) -> dict[str, QuerySet]:
    return {
        "tags": stat_tags(event_id),
        "grades": stat_grade(event_id),
        "jobs": stat_jobs(event_id),
        "tools": stat_tools(event_id),
    }
