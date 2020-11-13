from django.contrib import admin
from .models import Banner, Country, Destination
from adminsortable2.admin import SortableAdminMixin


@admin.register(Banner)
class BannerAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ('name', 'active')
    search_fields = ('name',)
    pass


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ('name', 'active')
    search_fields = ('name',)
    pass


@admin.register(Destination)
class DestinationAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ('title', 'sub_title', 'country', 'active')
    search_fields = ('title', 'sub_title', 'country__name')
    pass

