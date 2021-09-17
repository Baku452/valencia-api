from django.contrib import admin
from .models import (
    Package,
    PackageImage,
    PackageType,
    Month,
    Experience,
    Interest,
    Notification,
    OptionalImageRenting,
    OptionalRenting,
)
from itineraries.models import (
    Itinerary,
    Faq,
    DatesAndPrices,
    ItineraryImage,
)
from old_itinerario.models import ItineraryOld
from adminsortable2.admin import SortableAdminMixin
from modelclone import ClonableModelAdmin
from nested_inline.admin import NestedStackedInline, NestedModelAdmin


class DatesAndPricesAdmin(admin.StackedInline):
    model = DatesAndPrices
    extra = 0


class OptionalRentingAdmin(admin.StackedInline):
    model = OptionalRenting
    extra = 0


class FaqAdmin(admin.StackedInline):
    model = Faq
    extra = 0


# class ItineraryAdmin(admin.StackedInline):
#     model = Itinerary
#     extra = 0
# class ItineraryImageAdmin(NestedStackedInline):
#     model = ItineraryImage
#     extra = 0
#     fk_name = 'itinerary'
class ItineraryAdmin(admin.StackedInline):
    model = Itinerary
    extra = 0
    # inlines = [ItineraryImageAdmin]


class ItineraryOldAdmin(admin.StackedInline):
    model = ItineraryOld
    extra = 0


class PackageImageAdmin(admin.TabularInline):
    model = PackageImage
    extra = 0
    fields = ["image", "alt", "image_tag"]
    readonly_fields = ["image_tag"]
    inlines = ""


@admin.register(Package)
class PackageAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "rating",
        "days",
        "destination",
        "published",
        "optional",
        "travelZoo",
        "bookingWindow",
    )
    search_fields = ("title", "destination__title", "optional")
    inlines = [
        PackageImageAdmin,
        ItineraryAdmin,
        ItineraryOldAdmin,
        FaqAdmin,
        DatesAndPricesAdmin,
    ]
    # save_as = True
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


class OptionalRentingImageAdmin(NestedStackedInline):
    model = OptionalImageRenting
    extra = 0


@admin.register(OptionalRenting)
class OptionalRentingAdmin(admin.ModelAdmin):

    inlines = [OptionalRentingImageAdmin]

    class Meta:
        model = OptionalRenting


# Register your models here.
# admin.site.register(Package)
