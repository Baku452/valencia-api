from .models import Country, Banner, Destination
from rest_framework import serializers


class DestinationSerializer(serializers.ModelSerializer):
    #thumbnail = serializers.py.ImageField(read_only=True)

    class Meta:
        model = Destination
        fields = ['id', 'title', 'slug']


class CountrySerializer(serializers.ModelSerializer):

    destinations = DestinationSerializer(many=True, read_only=True)

    class Meta:
        model = Country
        fields = ['id', 'name', 'active', 'destinations']


class BannerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Banner
        fields = '__all__'
