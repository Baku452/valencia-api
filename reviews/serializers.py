from .models import (
    TripadvisorReviews
)
from rest_framework import serializers

class TripAdvisorSerializer(serializers.ModelSerializer):
    class Meta:
        model = TripadvisorReviews
        fields = "__all__"