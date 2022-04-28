from .models import Country, Banner, Destination, LandingPackage, LandingImages
from rest_framework import serializers
from packages.serializers import PackageLandingSerializer

class DestinationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Destination
        fields = "__all__"


class DestinationHomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Destination
        fields = ["id", "title", "sub_title", "slug", "active", "country","image","thumbnail"]


class CountrySerializer(serializers.ModelSerializer):

    destinations = DestinationHomeSerializer(many=True, read_only=True)

    class Meta:
        model = Country
        fields = ["id", "name", "active", "destinations"]

class BannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Banner
        fields = "__all__"

class LandingSerializer(serializers.ModelSerializer):
    destination = serializers.SlugRelatedField(
        many=False,
        read_only=True,
        slug_field='slug'
    )
    class Meta:
        model = LandingPackage
        fields = ["title", "titleSEO", "descriptionSEO","keywordsSEO",  "sub_title", "slug", "order", "content", "destination", "active"]

class LandingImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = LandingImages
        fields = ["id", "title", "image", "alt"]

class LandingRetrieveSerializer(serializers.ModelSerializer):
    images = LandingImageSerializer(many=True, read_only=True)
    package = PackageLandingSerializer()
    class Meta:
        model = LandingPackage
        fields = "__all__"
