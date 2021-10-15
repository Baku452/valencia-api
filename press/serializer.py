from .models import PressPost, Awards
from rest_framework import serializers


class PressPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = PressPost
        fields = "__all__"


class AwardsSerializaer(serializers.ModelSerializer):
    class Meta:
        model = Awards
        fields = "__all__"
