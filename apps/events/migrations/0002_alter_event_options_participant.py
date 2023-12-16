# Generated by Django 4.2 on 2023-12-16 10:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        (
            "specialists",
            "0002_alter_specialist_options_specialist_first_name_and_more",
        ),
        ("attributes", "0006_upload_tags_roles_status"),
        ("events", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="event",
            options={
                "default_related_name": "events",
                "verbose_name": "Мероприятие",
                "verbose_name_plural": "Мероприятия",
            },
        ),
        migrations.CreateModel(
            name="Participant",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "created_at",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="Дата создания"
                    ),
                ),
                (
                    "updated_at",
                    models.DateTimeField(
                        auto_now=True, verbose_name="Дата обновления"
                    ),
                ),
                (
                    "comment",
                    models.CharField(
                        max_length=255, verbose_name="Комментарии"
                    ),
                ),
                (
                    "event",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="events.event",
                        verbose_name="Мероприятие",
                    ),
                ),
                (
                    "role",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to="attributes.role",
                        verbose_name="Роль",
                    ),
                ),
                (
                    "specialist",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="specialists.specialist",
                        verbose_name="Участник",
                    ),
                ),
            ],
            options={
                "verbose_name": "Участник",
                "verbose_name_plural": "Участники",
                "ordering": ("-event_id", "role_id"),
                "default_related_name": "participants",
            },
        ),
    ]
