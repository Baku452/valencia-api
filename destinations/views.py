from rest_framework.views import APIView
from django.http import Http404
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK

from .models import Destination, Country, Banner, LandingPackage
from .serializers import CountrySerializer, BannerSerializer, DestinationSerializer, LandingSerializer, LandingRetrieveSerializer

def get_object(slug, model):
    try:
        return model.objects.get(slug=slug)
    except model.DoesNotExist:
        raise Http404

#Destinations
class DestinationListApi(APIView):
    def get(self, request):
        countries = Country.objects.filter(active=True)
        serializer = CountrySerializer(countries, many=True)
        return Response(serializer.data, status=HTTP_200_OK)


class DestinationsApi(APIView):
    def get(self, request):
        destinations = Destination.objects.filter(active=True)
        serializer = DestinationSerializer(destinations, many=True)
        return Response(serializer.data, status=HTTP_200_OK)

class DestinationRetrieveApi(APIView):
    def get(self, request, slug):
        destination = get_object(slug, Destination)
        serializer = DestinationSerializer(destination)
        return Response(serializer.data, status = HTTP_200_OK)

#Banner
class BannerListApi(APIView):
    def get(self, request):
        banners = Banner.objects.all().filter(active=True)
        serializer = BannerSerializer(banners, many=True)
        return Response(serializer.data, status=HTTP_200_OK)

#Landings
class LandingListApi(APIView):
    def get(self, request):
        landings = LandingPackage.objects.all().filter(active=True)
        serializer = LandingSerializer(landings, many=True)
        return Response(serializer.data, status=HTTP_200_OK)

#Landing
class LandingRetrieveApi(APIView):
    def get(self, request, slug):
        landing = get_object(slug, LandingPackage)
        serializer = LandingRetrieveSerializer(landing)
        return Response(serializer.data, status = HTTP_200_OK)