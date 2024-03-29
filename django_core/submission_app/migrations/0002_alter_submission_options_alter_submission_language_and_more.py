# Generated by Django 5.0 on 2023-12-17 16:41

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("submission_app", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="submission",
            options={
                "verbose_name": "Результат тестирования",
                "verbose_name_plural": "Результаты тестирований",
            },
        ),
        migrations.AlterField(
            model_name="submission",
            name="language",
            field=models.CharField(
                choices=[
                    ("python", "python"),
                    ("java", "java"),
                    ("C++", "C++"),
                    ("PHP", "PHP"),
                    ("C", "C"),
                    ("js", "js"),
                ],
                max_length=64,
                verbose_name="Язык программирования",
            ),
        ),
        migrations.AlterField(
            model_name="submission",
            name="worker_uuid",
            field=models.CharField(max_length=1024, verbose_name="UUID задачи воркера"),
        ),
    ]
