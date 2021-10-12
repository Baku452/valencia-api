from django.contrib import admin
from .models import Tailor
from adminsortable2.admin import SortableAdminMixin


# Register your models here.
@admin.register(Tailor)
class TailorAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ("title", "active")
    search_fields = ("title",)
