from rest_framework.serializers import ModelSerializer
from .models import Theory


class TheorySerializer(ModelSerializer):

    class Meta:
        model = Theory
        fields = "__all__"