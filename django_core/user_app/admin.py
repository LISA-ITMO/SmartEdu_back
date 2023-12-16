from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User

@admin.register(User)
class UserAdmin(BaseUserAdmin):
    ordering = ["email"]
    list_display = ["pk", "email", "type"]
    fieldsets = [
        (
            "Основная информация",
            {
                "fields": ("email", "password", "type")
            }
        ),
        (
            "Разрешения",
            {
                "fields": ("is_staff", "is_active", "groups")
            }
        )

    ]
    add_fieldsets = (
        (None, {"classes": ("wide",), "fields": ("email", "password1", "password2")}),
    )
