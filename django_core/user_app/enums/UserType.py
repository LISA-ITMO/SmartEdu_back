from django.db.models import TextChoices


class UserType(TextChoices):
    TEACHER = "Teacher", "Преподаватель"
    STUDENT = "Student", "Студент"
