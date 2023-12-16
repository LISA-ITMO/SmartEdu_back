# Generated by Django 5.0 on 2023-12-16 17:23

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lecture_app', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='theory',
            managers=[
            ],
        ),
        migrations.AlterField(
            model_name='theory',
            name='created_by',
            field=models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='theory', to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='TheoryPresentContent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_path', models.FileField(upload_to='')),
                ('theory', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='files', to='lecture_app.theory')),
            ],
        ),
        migrations.CreateModel(
            name='TheoryTextContent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('theory', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='text', to='lecture_app.theory')),
            ],
        ),
        migrations.CreateModel(
            name='TheoryVideoContent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_path', models.FileField(upload_to='')),
                ('url', models.URLField()),
                ('theory', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='videos', to='lecture_app.theory')),
            ],
        ),
    ]
