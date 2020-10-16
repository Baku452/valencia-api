from .models import Itinerary, ItineraryImage, ItineraryItems
from rest_framework import serializers


class ItineraryImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = ItineraryImage
        fields = '__all__'


class ItineraryItemseSerializer(serializers.ModelSerializer):

    class Meta:
        model = ItineraryItems
        fields = '__all__'


class ItinerarySerializer(serializers.ModelSerializer):
    images = ItineraryImageSerializer(many=True, read_only=True)
    items = ItineraryItemseSerializer(many=True, read_only=True)

    class Meta:
        model = Itinerary
        fields = '__all__'
