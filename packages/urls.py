from django.urls import path
from . import views

urlpatterns = [
    path("", views.PackageSearchApi.as_view(), name="packages-search"),
    path("<str:slug>", views.PackageRetrieveApi.as_view(), name="packages-retrieve"),
    path("home/", views.PackageHomeListApi.as_view(), name="packages-search"),
    path("titles/", views.PackageTitleApi.as_view(), name="packages-titles"),
    path("list/", views.PackageListApi.as_view(), name="packages-list"),
    path("optional/",views.PackageOptionalSearchApi.as_view(),name="packages-optional",),
    path("promo/", views.PackagePromoSearchApi.as_view(), name="packages-promo"),
    path("luxury/", views.PackageLuxuryApi.as_view(), name="packages-luxury"),
    path("top/<int:id>",views.PackagesTop.as_view(),name="packages-top",),
    path("promo/adventure/",views.PackagePromoAdventureSearchApi.as_view(),name="packages-promo",),
    #Package Types
    path("types/<str:slug>",views.PackageTypeRetrieve.as_view(),name="packages-type-retrieve"),
    path("types/", views.PackageTypeListApi.as_view(), name="packages-type-list"),
    path("types/<int:pk>",views.PackageTypeDetailApi.as_view(),name="packages-type-list"),
    path("types/nav/", views.PackageTypeNavApi.as_view(), name="packages-type-nav"),
    path("types/home/", views.PackageTypeHomeApi.as_view(), name="packages-type-home"),
]