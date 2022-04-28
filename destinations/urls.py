from django.urls import path
from . import views
from packages.views import DestinationPackagesTop

urlpatterns = [
    path("", views.DestinationListApi.as_view(), name="destination-list"),
    path("<str:slug>", views.DestinationRetrieveApi.as_view(), name="destination-retrieve"),
    path("<str:slug>/packages/top/", DestinationPackagesTop.as_view(), name="destination-top"),
    path("cities/all/", views.DestinationsApi.as_view(), name="destination-list-all"),
    path("banners/", views.BannerListApi.as_view(), name="banners-list"),
    path("landings/", views.LandingListApi.as_view(), name="landings-list"),
    path("landings/<str:slug>", views.LandingRetrieveApi.as_view(), name="landing-retrieve"),
]