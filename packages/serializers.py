from .models import (
    Package,
    PackageType,
    PackageImage,
    Experience,
    Interest,
    Notification,
    OptionalRenting,
    OptionalImageRenting,
)
from specialists.models import Specialist
from rest_framework import serializers
from old_itinerario.serializers import ItineraryOldSerializer
from itineraries.serializers import (
    ItinerarySerializer,
    FaqSerializer,
    DatesAndPricesSerializer,
)

#Serializer Package Type
class PackageTypeRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = PackageType
        fields = "__all__"

class OptionalRentingImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = OptionalImageRenting
        fields = "__all__"


class OptionalRentingSerializer(serializers.ModelSerializer):
    images = OptionalRentingImageSerializer(many=True, read_only=True)

    class Meta:
        model = OptionalRenting
        fields = "__all__"


class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = ["id", "title", "slug"]


class NotificationContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = ["id", "title", "slug", "content"]


class InterestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Interest
        fields = "__all__"


class ExperienceSerializer(serializers.ModelSerializer):
    thumbnail = serializers.ImageField(read_only=True)

    class Meta:
        model = Experience
        fields = "__all__"


class PackageSerializer(serializers.ModelSerializer):
    thumbnail = serializers.ImageField(read_only=True)
    type_name = serializers.StringRelatedField(many=True, source="package_type")
    destination_name = serializers.StringRelatedField(source="destination")
    activity_name = serializers.CharField(source="get_activity_display")

    class Meta:
        model = Package
        fields = "__all__"


class PackageHomeSerializer(serializers.ModelSerializer):
    thumbnail = serializers.ImageField(read_only=True)

    class Meta:
        model = Package
        fields = ["title", "slug", "days", "thumbnail", "summary"]


class PackageTitleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Package
        fields = ["title", "slug", "days", "package_type"]


class PackageTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PackageType
        fields = "__all__"


class PackageTypeHomeSerializer(serializers.ModelSerializer):
    thumbnail = serializers.ImageField(read_only=True)

    class Meta:
        model = PackageType
        fields = ["id", "slug","thumbnail", "title", "content", "svg"]


class PackageTypeNavSerializer(serializers.ModelSerializer):
    class Meta:
        model = PackageType
        fields = ["id", "title", "svg", "slug"]


class PackageImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PackageImage
        fields = ["id", "image", "alt"]


class SpecialistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Specialist
        fields = "__all__"


class PackageDetailSerializer(serializers.ModelSerializer):

    images = PackageImageSerializer(many=True, read_only=True)
    specialist = SpecialistSerializer()
    itineraries = ItinerarySerializer(many=True, read_only=True)
    old_itinerario = ItineraryOldSerializer(many=True, read_only=True)
    related_packages = PackageSerializer(many=True, read_only=True)
    faqs = FaqSerializer(many=True, read_only=True)
    optional_forRenting = OptionalRentingSerializer(many=True, read_only=True)
    dates_prices = DatesAndPricesSerializer(many=True, read_only=True)
    destination_name = serializers.StringRelatedField(source="destination")
    type_name = serializers.StringRelatedField(many=True, source="package_type")
    activity_name = serializers.CharField(source="get_activity_display")

    class Meta:
        model = Package
        fields = "__all__"

class PackageLandingSerializer(serializers.ModelSerializer):

    itineraries = ItinerarySerializer(many=True, read_only=True)

    class Meta:
        model = Package
        fields = ["id", "slug", "title", "summary","fixedDepartures", "price","days","description", "highligths" , "itineraries" ,"videoURL", "whats_not_included", "whats_included" ,"itineraries"]

class PackageDetailTypesSerializer(serializers.ModelSerializer):

    package_type = PackageTypeSerializer(many=True, read_only=True)

    class Meta:
        model = Package
        fields = "__all__"
