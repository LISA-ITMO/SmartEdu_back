from django.db import models


class TheoryType(models.Model):
    title = models.CharField(max_length=1024)


class Theory(models.Model):
    title = models.CharField(max_length=1024)
    desc = models.TextField(null=True)
    time_to_read = models.IntegerField(default=300)  # 5 minutes
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey("user_app.User",
                                   null=True,
                                   related_name='theory',
                                   default=1,
                                   on_delete=models.SET_NULL)
    theory_type = models.ForeignKey(TheoryType,
                                    null=True,
                                    on_delete=models.SET_NULL)


class TheoryPresentContent(models.Model):
    theory = models.ForeignKey(Theory,
                               null=True,
                               on_delete=models.SET_NULL,
                               related_name="files")
    file_path = models.FileField()


class TheoryVideoContent(models.Model):
    theory = models.ForeignKey(Theory,
                               null=True,
                               on_delete=models.SET_NULL,
                               related_name="videos")
    file_path = models.FileField()
    url = models.URLField()


class TheoryTextContent(models.Model):
    theory = models.ForeignKey(Theory,
                               null=True,
                               on_delete=models.SET_NULL,
                               related_name="text")
    content = models.TextField()
