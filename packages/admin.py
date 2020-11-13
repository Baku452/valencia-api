from django.contrib import admin
from .models import Package, PackageImage, PackageType, Month, Experience, Interest, Notification
from itineraries.models import Itinerary
from adminsortable2.admin import SortableAdminMixin


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
    list_display = ('title', 'destination', 'published')
    search_fields = ('title', 'destination__title', )
    inlines = [PackageImageAdmin, ItineraryAdmin]

    class Meta:
        model = Package


@admin.register(PackageType)
class PackageTypeAdmin(SortableAdminMixin, admin.ModelAdmin):
    pass


@admin.register(Month)
class MonthAdmin(admin.ModelAdmin):
    pass


@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    pass


@admin.register(Interest)
class InterestAdmin(SortableAdminMixin, admin.ModelAdmin):
    pass


@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    pass




# Register your models here.
# admin.site.register(Package)