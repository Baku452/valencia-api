from django.contrib import admin
from .models import Banner, Country, Destination, LandingPackage, LandingImages
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

class LandingImageAdmin(admin.TabularInline):
    model = LandingImages
    extra = 0
    fields = ["image", "title", "alt", "image_tag"]
    readonly_fields = ["image_tag"]
    inlines = ""

@admin.register(LandingPackage)
class LandingPackageAdmin(SortableAdminMixin, admin.ModelAdmin):
    search_fields = ('title', 'sub_title', 'country__name')
    inlines = [
        LandingImageAdmin
    ]
    pass

