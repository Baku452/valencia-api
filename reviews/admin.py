from django.contrib import admin
from .models import TripadvisorReviews

# Register your models here.
@admin.register(TripadvisorReviews)
class TripadvisorReviews(admin.ModelAdmin):
    
    list_display = ["title","published", "rating", "url"]
    pass