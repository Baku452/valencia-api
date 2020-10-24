from django.contrib import admin
from .models import Banner, Country, Destination
from adminsortable2.admin import SortableAdminMixin


@admin.register(Banner)
class BannerAdmin(SortableAdminMixin, admin.ModelAdmin):
    pass


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    pass


@admin.register(Destination)
class DestinationAdmin(SortableAdminMixin, admin.ModelAdmin):
    pass
