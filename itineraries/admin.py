from django.contrib import admin
from .models import Itinerary, ItineraryImage


class ItineraryImageAdmin(admin.StackedInline):
    model = ItineraryImage
    extra = 0


@admin.register(Itinerary)
class ItineraryAdmin(admin.ModelAdmin):
    list_display = ('subtitle', 'package', 'active')
    search_fields = ('subtitle', 'package__title', )
    inlines = [ItineraryImageAdmin]

    class Meta:
        model = Itinerary


@admin.register(ItineraryImage)
class ItineraryImageAdmin(admin.ModelAdmin):
    pass
# Register your models here.
# admin.site.register(Package)