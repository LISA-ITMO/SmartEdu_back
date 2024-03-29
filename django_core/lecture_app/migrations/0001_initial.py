# Generated by Django 4.1.13 on 2023-12-12 08:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="TheoryType",
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
                ("title", models.CharField(max_length=1024)),
            ],
            options={"abstract": False,},
        ),
        migrations.CreateModel(
            name="Theory",
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
                ("title", models.CharField(max_length=1024)),
                ("desc", models.TextField(null=True)),
                ("time_to_read", models.IntegerField(default=300)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "created_by",
                    models.ForeignKey(
                        default=1,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="Author",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "theory_type",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="lecture_app.theorytype",
                    ),
                ),
            ],
            options={"abstract": False,},
            managers=[("theory_content", django.db.models.manager.Manager()),],
        ),
    ]
