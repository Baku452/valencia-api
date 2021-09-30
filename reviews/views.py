from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import (
    TripadvisorReviews,
)
from .serializers import (
    TripAdvisorSerializer,
)

# Create your views here.

class TripadvisorReviewAPI(APIView):
    def get(self, request):
        reviews = TripadvisorReviews.objects.all().filter(published=True)
        serializer = TripAdvisorSerializer(reviews, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)