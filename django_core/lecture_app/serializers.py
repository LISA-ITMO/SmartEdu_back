from rest_framework.serializers import ModelSerializer

from .models import (
    Theory,
    TheoryType,
    TheoryPresentContent,
    TheoryVideoContent,
    TheoryTextContent,
)


class TheorySerializer(ModelSerializer):
    class Meta:
        model = Theory
        fields = "__all__"


class TheoryTypeSerializer(ModelSerializer):
    class Meta:
        model = TheoryType
        fields = "__all__"


class TheoryPresentContentSerializer(ModelSerializer):
    class Meta:
        model = TheoryPresentContent
        fields = ("file_path",)


class TheoryVideoContentSerializer(ModelSerializer):
    class Meta:
        model = TheoryVideoContent
        fields = ("file_path", "url")


class TheoryTextContentSerializer(ModelSerializer):
    class Meta:
        model = TheoryTextContent
        fields = ("content",)
