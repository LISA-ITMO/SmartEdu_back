from django.db import models
from django.contrib.auth.models import User
from djongo import models


# Create your models here.

class TheoryType(models.Model):
    title = models.CharField(max_length=1024)

    class Meta:
        abstract = False


class Theory(models.Model):
    title = models.CharField(max_length=1024)
    desc = models.TextField(null=True)
    time_to_read = models.IntegerField(default=300)  # 5 minutes
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, null=True, related_name='Author', default=1, on_delete=models.SET_NULL)
    theory_type = models.ForeignKey(TheoryType, null=True, on_delete=models.SET_NULL)
    theory_content = models.DjongoManager()

    class Meta:
        abstract = False


class TheoryPresentContent(models.Model):
    theory = models.ForeignKey(Theory, null=True, on_delete=models.SET_NULL)
    file_path = models.FileField()

    class Meta:
        abstract = True


class TheoryVideoContent(models.Model):
    theory = models.ForeignKey(Theory, null=True, on_delete=models.SET_NULL)
    file_path = models.FileField()
    url = models.TextField(max_length=255)

    class Meta:
        abstract = True


class TheoryTextContent(models.Model):
    theory = models.ForeignKey(Theory, null=True, on_delete=models.SET_NULL)
    content = models.TextField()

    class Meta:
        abstract = True
