# Generated by Django 5.0 on 2023-12-17 15:03

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("lecture_app", "0002_alter_theory_managers_alter_theory_created_by_and_more"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="theory",
            options={"verbose_name": "Теория", "verbose_name_plural": "Теории"},
        ),
        migrations.AlterModelOptions(
            name="theorypresentcontent",
            options={
                "verbose_name": "Файл для теории",
                "verbose_name_plural": "Файлы для теории",
            },
        ),
        migrations.AlterModelOptions(
            name="theorytextcontent",
            options={
                "verbose_name": "Текстовый контент для теории",
                "verbose_name_plural": "Текстовый контент для теории",
            },
        ),
        migrations.AlterModelOptions(
            name="theorytype",
            options={
                "verbose_name": "Тип теории",
                "verbose_name_plural": "Типы теории",
            },
        ),
        migrations.AlterModelOptions(
            name="theoryvideocontent",
            options={
                "verbose_name": "Видео для теории",
                "verbose_name_plural": "Видео для теории",
            },
        ),
    ]
