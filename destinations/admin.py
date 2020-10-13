from django.contrib import admin
from .models import Banner, Country, Destination


@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    pass


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    pass


@admin.register(Destination)
class DestinationAdmin(admin.ModelAdmin):
    pass
