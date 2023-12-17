# Generated by Django 5.0 on 2023-12-17 16:41

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Tag",
            fields=[
                (
                    "name",
                    models.CharField(max_length=128, primary_key=True, serialize=False),
                ),
            ],
            options={
                "verbose_name": "Тэг",
                "verbose_name_plural": "Тэги",
            },
        ),
    ]
