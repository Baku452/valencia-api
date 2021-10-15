from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import PressPost, Awards

# Create your views here.

from .serializer import PressPostSerializer, AwardsSerializaer


class AwardsListApi(APIView):
    def get(self, request):
        awards = Awards.objects.all()
        serializer = AwardsSerializaer(awards, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class PressPostsListApi(APIView):
    def get(self, request):
        posts = PressPost.objects.all()
        serializer = PressPostSerializer(posts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
