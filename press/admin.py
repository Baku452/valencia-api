from django.contrib import admin
from adminsortable2.admin import SortableAdminMixin

from .models import PressPost, Awards

# Register your models here.


@admin.register(PressPost)
class PressAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ("title", "author")
    search_fields = ("title", "author")

    class Meta:
        model = PressPost


@admin.register(Awards)
class AwardAdmin(SortableAdminMixin, admin.ModelAdmin):
    # search_fields = "title"

    class Meta:
        model = Awards
