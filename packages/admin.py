from django.contrib import admin
from .models import Package, PackageImage, PackageType, Month, Experience
from itineraries.models import Itinerary, ItineraryImage


class ItineraryAdmin(admin.StackedInline):
    model = Itinerary
    extra = 0


class PackageImageAdmin(admin.TabularInline):
    model = PackageImage
    extra = 0
    fields = ['image', 'alt', 'image_tag']
    readonly_fields = ['image_tag']


@admin.register(Package)
class PackageAdmin(admin.ModelAdmin):
    list_display = ('title', 'published')
    inlines = [PackageImageAdmin, ItineraryAdmin]

    class Meta:
        model = Package


@admin.register(PackageType)
class PackageTypeAdmin(admin.ModelAdmin):
    pass


@admin.register(Month)
class MonthAdmin(admin.ModelAdmin):
    pass


@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    pass

#@admin.register(PackageImage)
#class PackageImageAdmin(admin.ModelAdmin):
#    pass

# Register your models here.
# admin.site.register(Package)