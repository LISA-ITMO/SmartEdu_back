from django.contrib import admin

from .models import Task, CodeTask, TestCase, TaskType


class CodeTaskInLine(admin.TabularInline):
    model = CodeTask
    extra = 0


class TestCaseInLine(admin.TabularInline):
    model = TestCase
    extra = 0


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    inlines = [
        CodeTaskInLine,
    ]


@admin.register(CodeTask)
class CodeTaskAdmin(admin.ModelAdmin):
    inlines = [
        TestCaseInLine,
    ]


@admin.register(TaskType)
class TaskType(admin.ModelAdmin):
    pass
