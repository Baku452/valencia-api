from .models import ContactUs, Newsletter, ContactUsB2C, ContactUsB2B, TailorForm
from rest_framework import serializers
from packages.models import PackageType


class ContactUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactUs
        fields = '__all__'

class ContactUsB2BSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactUsB2B
        fields = '__all__'

class ContactUsB2CSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactUsB2C
        fields = '__all__'

class TailorFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = TailorForm
        fields = '__all__'

class NewsletterSerializer(serializers.ModelSerializer):

    package_type = serializers.PrimaryKeyRelatedField(
         many=True,
         queryset=PackageType.objects.all()
    )

    class Meta:
        model = Newsletter
        fields = '__all__'
