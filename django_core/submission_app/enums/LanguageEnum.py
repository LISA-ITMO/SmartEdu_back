from django.db.models import TextChoices


class LanguageEnum(TextChoices):
    PYTHON = "python", "java"
    JAVA = "java", "java"
    CPP = "C++", "C++"
    PHP = "PHP", "PHP"
    C = "C", "C"
    JS = "js", "js"

