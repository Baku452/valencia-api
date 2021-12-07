from django.contrib import admin
from .models import Blog, BlogType, Blogger, BlogInterest
from adminsortable2.admin import SortableAdminMixin
from modelclone import ClonableModelAdmin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

# Register your models here.


@admin.register(Blog)
class BlogAdmin(ClonableModelAdmin):
    # exclude = ('author',)
    list_display = ("title", "published")
    search_fields = ("title", "destination__title")

    def save_model(self, request, obj, form, change):
        if not change:
            obj.author = request.user
        obj.save()

    # save_as = True
    class Meta:
        model = Blog


@admin.register(BlogType)
class BlogTypeAdmin(SortableAdminMixin, admin.ModelAdmin):
    pass


@admin.register(BlogInterest)
class BlogInterestAdmin(SortableAdminMixin, admin.ModelAdmin):
    pass


class BloggerInline(admin.StackedInline):
    model = Blogger
    can_delete = False
    verbose_name_plural = "employee"


class UserAdmin(BaseUserAdmin):
    inlines = (BloggerInline,)


admin.site.unregister(User)
admin.site.register(Blogger)
admin.site.register(User, UserAdmin)
