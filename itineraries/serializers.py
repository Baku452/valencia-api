from .models import Itinerary, ItineraryImage
from rest_framework import serializers


class ItineraryImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = ItineraryImage
        fields = '__all__'


class ItinerarySerializer(serializers.ModelSerializer):
    images = ItineraryImageSerializer(many=True, read_only=True)

    class Meta:
        model = Itinerary
        fields = '__all__'
