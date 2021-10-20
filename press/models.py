from django.db import models
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill
import os

# Create your models here.
def path_and_rename(instance, filename):
    upload_to = "images/press/"
    ext = filename.split(".")[-1]
    if instance.pk:
        filename = "{}.{}".format(instance.title, ext)
    else:
        filename = "{}.{}".format(instance.title, ext)
    return os.path.join(upload_to, filename)


def path_and_renameAward(instance, filename):
    upload_to = "images/awards/"
    ext = filename.split(".")[-1]
    if instance.pk:
        filename = "{}.{}".format(instance.title, ext)
    else:
        filename = "{}.{}".format(instance.title, ext)
    return os.path.join(upload_to, filename)


class PressPost(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    date = models.DateField()
    url = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    authorLink = models.CharField(max_length=255)
    image = ProcessedImageField(
        upload_to=path_and_rename,
        processors=[ResizeToFill(380, 250)],
        format="JPEG",
        options={"quality": 100},
        blank=True,
    )
    order = models.PositiveIntegerField(default=0, blank=False, null=False)

    class Meta:
        ordering = ["order"]

    def __str__(self):
        return self.title


class Awards(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    date = models.DateField()
    url = models.CharField(max_length=255)
    image = ProcessedImageField(
        upload_to=path_and_renameAward,
        processors=[ResizeToFill(585, 384)],
        format="JPEG",
        options={"quality": 100},
        blank=True,
    )

    order = models.PositiveIntegerField(default=0, blank=False, null=False)

    class Meta:
        ordering = ["order"]

    def __str__(self):
        return self.title
