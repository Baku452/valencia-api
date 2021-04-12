from django.contrib import admin
from .models import Blog, BlogType

# Register your models here.

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'published')
    search_fields = ('title', 'destination__title')
    # save_as = True
    class Meta:
        model = Blog
