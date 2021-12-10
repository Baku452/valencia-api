from django.db import models
from tinymce.models import HTMLField
from django.utils.html import mark_safe
from imagekit.models import ImageSpecField, ProcessedImageField
from autoslug import AutoSlugField
from imagekit.processors import ResizeToFill
from destinations.models import Destination
from django.core.validators import FileExtensionValidator
from smart_selects.db_fields import ChainedForeignKey
from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import User
import os


# Create your models here.
def path_and_rename(instance, filename):
    upload_to = "images/blog-thumbnail/"
    ext = filename.split(".")[-1]
    if instance.pk:
        filename = "{}.{}".format(instance.slug, ext)
    else:
        filename = "{}.{}".format(instance.slug, ext)
    return os.path.join(upload_to, filename)


def path_and_rename_package(instance, filename):

    upload_to = "images/blog/"
    ext = filename.split(".")[-1]
    if instance.pk:
        filename = "{}.{}".format(instance.slug, ext)
    else:
        filename = "{}.{}".format(instance.slug, ext)
    return os.path.join(upload_to, filename)


class Blogger(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    biography = models.TextField()
    image = ProcessedImageField(
        upload_to="images/blogger/",
        processors=[ResizeToFill(400, 600)],
        format="JPEG",
        options={"quality": 95},
        blank=True,
    )

    def __str__(self):
        return self.user.username


class BlogType(models.Model):
    title = models.CharField(max_length=255)
    active = models.BooleanField(default=False)
    order = models.PositiveIntegerField(default=0, blank=False, null=False)
    slug = AutoSlugField(
        populate_from="title", unique_with=["title"], always_update=True
    )
    thumbnail = ProcessedImageField(
        upload_to=path_and_rename,
        processors=[ResizeToFill(380, 250)],
        format="JPEG",
        options={"quality": 95},
        blank=True,
    )
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "blog_type"
        ordering = ["order"]

    def __str__(self):
        return self.title


class BlogInterest(models.Model):
    title = models.CharField(max_length=255)
    active = models.BooleanField(default=False)
    order = models.PositiveIntegerField(default=0, blank=False, null=False)
    slug = AutoSlugField(
        populate_from="title", unique_with=["title"], always_update=True
    )
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "blog_interest"
        ordering = ["order"]

    def __str__(self):
        return self.title


class Blog(models.Model):
    title = models.CharField(max_length=255, default="")
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    time_reading = models.IntegerField(default=0, blank=True)
    keywords = models.TextField(default="", blank=True)
    titleSEO = models.TextField(max_length=255, default="", blank=True)
    summary = models.TextField(max_length=255, default="")
    slug = AutoSlugField(
        populate_from="title", unique_with=["title"], always_update=True
    )

    content = RichTextUploadingField()
    blog_type = models.ForeignKey(
        BlogType, on_delete=models.CASCADE, null=True, blank=True
    )
    blog_interest = models.ManyToManyField(BlogInterest, blank=True)
    thumbnail = ProcessedImageField(
        upload_to=path_and_rename,
        processors=[ResizeToFill(800, 450)],
        format="JPEG",
        options={"quality": 95},
        blank=True,
    )
    thumbnail_cat = ImageSpecField(
        source="thumbnail",
        processors=[ResizeToFill(385, 217)],
        format="JPEG",
        options={"quality": 95},
    )
    banner = ProcessedImageField(
        upload_to=path_and_rename,
        processors=[ResizeToFill(1900, 500)],
        format="JPEG",
        blank=True,
    )
    destination = models.ForeignKey(
        Destination,
        default=None,
        on_delete=models.CASCADE,
    )
    popular = models.BooleanField(default=False)
    published = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "blog_posts"

    def __str__(self):
        return self.title
