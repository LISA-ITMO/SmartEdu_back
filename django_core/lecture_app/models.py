from django.db import models


class TheoryType(models.Model):
    title = models.CharField(max_length=1024)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Тип теории"
        verbose_name_plural = "Типы теории"


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

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Теория"
        verbose_name_plural = "Теории"


class TheoryPresentContent(models.Model):
    theory = models.ForeignKey(Theory,
                               null=True,
                               on_delete=models.SET_NULL,
                               related_name="files")
    file_path = models.FileField()

    def __str__(self):
        return f"Файлы для {self.theory.title}"

    class Meta:
        verbose_name = "Файл для теории"
        verbose_name_plural = "Файлы для теории"


class TheoryVideoContent(models.Model):
    theory = models.ForeignKey(Theory,
                               null=True,
                               on_delete=models.SET_NULL,
                               related_name="videos")
    file_path = models.FileField()
    url = models.URLField()

    def __str__(self):
        return f"Видео контент для {self.theory.title}"

    class Meta:
        verbose_name = "Видео для теории"
        verbose_name_plural = "Видео для теории"


class TheoryTextContent(models.Model):
    theory = models.ForeignKey(Theory,
                               null=True,
                               on_delete=models.SET_NULL,
                               related_name="text")
    content = models.TextField()

    def __str__(self):
        return f"Текстовый контент для {self.theory.title}"

    class Meta:
        verbose_name = "Текстовый контент для теории"
        verbose_name_plural = "Текстовый контент для теории"

