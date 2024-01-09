# Generated by Django 5.0 on 2023-12-17 21:30

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        (
            "submission_app",
            "0002_alter_submission_options_alter_submission_language_and_more",
        ),
    ]

    operations = [
        migrations.AddField(
            model_name="submission",
            name="output",
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name="submission",
            name="status",
            field=models.CharField(
                choices=[
                    ("PENDING", "Ожидание"),
                    ("SUCCESS", "Успех"),
                    ("ERROR", "Ошибка"),
                ],
                default="PENDING",
                max_length=64,
                verbose_name="Статус",
            ),
        ),
    ]
