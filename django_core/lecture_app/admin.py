from django.contrib import admin
from .models import Theory, TheoryTextContent, TheoryPresentContent, TheoryVideoContent, TheoryType


class TheoryTextContentInline(admin.TabularInline):
    model = TheoryTextContent
    extra = 0


class TheoryPresentContentInline(admin.TabularInline):
    model = TheoryPresentContent
    extra = 0


class TheoryVideoContentInLine(admin.TabularInline):
    model = TheoryVideoContent
    extra = 0


@admin.register(Theory)
class TheoryAdmin(admin.ModelAdmin):
    inlines = [
        TheoryTextContentInline,
        TheoryPresentContentInline,
        TheoryVideoContentInLine
    ]


@admin.register(TheoryType)
class TheoryTypeAdmin(admin.ModelAdmin):
    pass