# Generated by Django 4.2 on 2023-12-16 10:24

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("attributes", "0006_upload_tags_roles_status"),
        ("specialists", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="specialist",
            options={
                "default_related_name": "specialists",
                "verbose_name": "Специалист",
                "verbose_name_plural": "Специалисты",
            },
        ),
        migrations.AddField(
            model_name="specialist",
            name="first_name",
            field=models.CharField(
                blank=True, max_length=50, verbose_name="Имя"
            ),
        ),
        migrations.AddField(
            model_name="specialist",
            name="last_name",
            field=models.CharField(
                blank=True, max_length=50, verbose_name="Фамилия"
            ),
        ),
        migrations.AlterField(
            model_name="specialist",
            name="tools",
            field=models.ManyToManyField(
                blank=True, to="attributes.tool", verbose_name="Инструменты"
            ),
        ),
    ]
