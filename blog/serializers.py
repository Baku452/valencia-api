from .models import Blog, BlogType
from rest_framework import serializers
from django.contrib.auth.models import User
from django.db.models.functions import Concat
class BlogDetailSerializer(serializers.ModelSerializer):
    first_name = serializers.ReadOnlyField(source="author.first_name")
    last_name = serializers.ReadOnlyField(source="author.last_name")
    destination = serializers.SlugRelatedField(read_only=True, slug_field='title')
    blog_type = serializers.SlugRelatedField(many=True, read_only=True, slug_field='title')
    created = serializers.DateTimeField(format="%d-%m-%Y", required=False, read_only=True)
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
    # thumbnail = serializers.ImageField(read_only=True)
    first_name = serializers.ReadOnlyField(source="author.first_name")
    last_name = serializers.ReadOnlyField(source="author.last_name")
    blog_type = serializers.SlugRelatedField(many=True, read_only=True, slug_field='title')
    destination = serializers.SlugRelatedField(read_only=True, slug_field='title')
    class Meta:
        model = Blog
        fields = '__all__'