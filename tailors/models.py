from django.db import models

# Create your models here.
from django.db import models
from tinymce.models import HTMLField
from imagekit.models import ImageSpecField, ProcessedImageField
from imagekit.processors import ResizeToFill
from autoslug import AutoSlugField
import os


def path_and_rename(instance, filename):
    upload_to = "images/tailor/"
    ext = filename.split(".")[-1]
    filename = "{}.{}".format(instance.title, ext)
    return os.path.join(upload_to, filename)


class Tailor(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(default="")
    image = ProcessedImageField(
        blank=True,
        null=True,
        upload_to=path_and_rename,
        processors=[ResizeToFill(490, 250)],
        format="JPEG",
        options={"quality": 100},
    )

    active = models.BooleanField(default=False)
    order = models.PositiveIntegerField(default=0, blank=False, null=False)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "tailor"
        ordering = ["order"]

    def __str__(self):
        return self.title
