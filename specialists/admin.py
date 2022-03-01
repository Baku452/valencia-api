from django.contrib import admin
from .models import (
    Specialist,
    ContactUs,
    ContactUsB2C,
    ContactUsB2B,
    TailorForm,
    Newsletter,
)

# Register your models here.


@admin.register(Specialist)
class SpecialistAdmin(admin.ModelAdmin):
    pass


@admin.register(ContactUs)
class ContactUsAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "email", "created")
    readonly_fields = (
        "first_name",
        "last_name",
        "email",
        "country_residence",
        "destination_interest",
        "description",
        "typeClient",
        "company",
        "is_newsletter",
    )
    pass


@admin.register(ContactUsB2C)
class ContactUsB2CAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "email", "created")
    readonly_fields = (
        "first_name",
        "last_name",
        "email",
        "country",
        "state",
        "number",
        "city",
        "description",
        "typeClient",
        "company",
        "is_newsletter",
    )
    pass


@admin.register(ContactUsB2B)
class ContactUsB2BAdmin(admin.ModelAdmin):
    list_display = ("first_name", "email", "created")
    readonly_fields = (
        "first_name",
        "last_name",
        "email",
        "number",
        "company",
        "message",
    )
    pass


@admin.register(TailorForm)
class TailorAdmin(admin.ModelAdmin):
    readonly_fields = (
        "first_name",
        "last_name",
        "email",
        "number",
        "destination_interest",
        "accommodation",
        "departureDate",
        "lengthStay",
        "adults",
        "children",
        "internationalFlight",
        "budget",
        "trip_type",
        "hear_about",
        "message",
    )
    pass


@admin.register(Newsletter)
class NewsletterAdmin(admin.ModelAdmin):
    list_display = ("first_name", "email", "created")
    readonly_fields = ("first_name", "last_name", "email")
    pass


# Register your models here.
