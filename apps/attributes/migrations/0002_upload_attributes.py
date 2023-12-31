# Generated by Django 4.2 on 2023-12-15 22:01

from django.db import migrations, models

from apps.core.utils import (
    get_cities_datasets,
    get_grades_datasets,
    get_jobs_datasets,
    get_tools_datasets,
)


def create_cities(apps, schema_editor):
    City: models.Model = apps.get_model("attributes", "City")
    datasets = get_cities_datasets()
    if datasets:
        types = [City(**fields) for fields in datasets]
        City.objects.bulk_create(types, ignore_conflicts=True)


def create_grades(apps, schema_editor):
    Grade: models.Model = apps.get_model("attributes", "Grade")
    datasets = get_grades_datasets()
    if datasets:
        types = [Grade(**fields) for fields in datasets]
        Grade.objects.bulk_create(types, ignore_conflicts=True)


def create_jobs(apps, schema_editor):
    Job: models.Model = apps.get_model("attributes", "Job")
    datasets = get_jobs_datasets()
    if datasets:
        types = [Job(**fields) for fields in datasets]
        Job.objects.bulk_create(types, ignore_conflicts=True)


def create_tools(apps, schema_editor):
    Tool: models.Model = apps.get_model("attributes", "Tool")
    datasets = get_tools_datasets()
    if datasets:
        types = [Tool(**fields) for fields in datasets]
        Tool.objects.bulk_create(types, ignore_conflicts=True)


class Migration(migrations.Migration):
    dependencies = [
        ("attributes", "0001_initial"),
    ]

    operations = [
        migrations.RunPython(create_cities),
        migrations.RunPython(create_grades),
        migrations.RunPython(create_jobs),
        migrations.RunPython(create_tools),
    ]
