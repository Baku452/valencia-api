from .models import Blog, BlogType
from rest_framework import serializers

class BlogDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = '__all__'

class BlogTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = BlogType
        fields = '__all__'

class BlogDetailTypesSerializer(serializers.ModelSerializer):

    blog_type = BlogTypeSerializer(many=True, read_only=True)

    class Meta:
        model = Blog
        fields = '__all__'

class BlogSerializer(serializers.ModelSerializer):
    thumbnail = serializers.ImageField(read_only=True)

    class Meta:
        model = Blog
        fields = '__all__'