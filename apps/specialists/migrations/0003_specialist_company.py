# Generated by Django 4.2 on 2023-12-16 11:51

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        (
            "specialists",
            "0002_alter_specialist_options_specialist_first_name_and_more",
        ),
    ]

    operations = [
        migrations.AddField(
            model_name="specialist",
            name="company",
            field=models.CharField(
                blank=True, max_length=60, verbose_name="Компания"
            ),
        ),
    ]
