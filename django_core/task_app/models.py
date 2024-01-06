from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class TaskType(models.Model):
    """
    Contains available type for the task
    """

    title = models.CharField(max_length=1024, primary_key=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Тип задания"
        verbose_name_plural = "Типы заданий"


class Task(models.Model):
    """
    Represent Task for displaying on frontend.
    """

    name = models.CharField(max_length=1024)
    difficulty = models.PositiveIntegerField(
        default=1, validators=[MaxValueValidator(10), MinValueValidator(1)]
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(editable=True, auto_now_add=True)
    created_by = models.ForeignKey(
        "user_app.User", on_delete=models.SET_NULL, related_name="tasks", null=True
    )
    description = models.TextField(null=True, blank=True)
    type = models.ForeignKey(TaskType, null=True, on_delete=models.SET_NULL)
    tags = models.ManyToManyField("tags_app.Tag")

    def __str__(self):
        return f"{self.name} ({self.type})"

    class Meta:
        verbose_name = "Задача"
        verbose_name_plural = "Задачи"


class CodeTask(models.Model):
    """
    Represent conditions for the Task.
    """

    task = models.OneToOneField(
        Task, on_delete=models.CASCADE, related_name="code_task"
    )
    content = models.TextField()

    def __str__(self):
        return f'Условие "{self.task.name}"'

    class Meta:
        verbose_name = "Условие задачи"
        verbose_name_plural = "Условия задач"


class TestCase(models.Model):
    """
    Represent test cases for Testing and submission CodeTask.
    """

    code_task = models.ForeignKey(
        CodeTask, on_delete=models.CASCADE, related_name="test_cases"
    )
    content = models.JSONField()

    class Meta:
        verbose_name = "Тест для задачи"
        verbose_name_plural = "Тесты для задач"
