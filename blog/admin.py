from django.contrib import admin
from .models import Blog, BlogType
from adminsortable2.admin import SortableAdminMixin
from modelclone import ClonableModelAdmin
# Register your models here.

@admin.register(Blog)
class BlogAdmin(ClonableModelAdmin):
    list_display = ('title', 'published')
    search_fields = ('title', 'destination__title')
    # save_as = True
    class Meta:
        model = Blog

@admin.register(BlogType)
class BlogTypeAdmin(SortableAdminMixin, admin.ModelAdmin):
    pass