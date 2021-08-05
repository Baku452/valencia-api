from django.db import models
from tinymce.models import HTMLField
from autoslug import AutoSlugField

# Create your models here.
class Page(models.Model):
    title = models.CharField(max_length=255, default="")
    keywords = models.TextField(default="")
    titleSEO = models.TextField(max_length=255, default="", blank=True)
    content = HTMLField(default=None, blank=True)
    slug = AutoSlugField(
        populate_from="title",
        unique_with=["title"],
    )
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "page"

    def __str__(self):
        return self.title
