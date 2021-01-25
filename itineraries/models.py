from django.db import models
from tinymce.models import HTMLField
from packages.models import Package
from imagekit.models import ProcessedImageField
from autoslug import AutoSlugField
from imagekit.processors import ResizeToFill
import os

ITINERARY_CHOICES = (
    ("Meals Included", "Meals Included"),
    ("Accommodations", "Accommodations"),
)


def path_and_rename(instance, filename):
    upload_to = 'images/itinerary/'
    ext = filename.split('.')[-1]
    if instance.pk:
        filename = '{}.{}'.format(instance.slug, ext)
    else:
        filename = '{}.{}'.format(instance.slug, ext)
    return os.path.join(upload_to, filename)


class Itinerary(models.Model):

    package = models.ForeignKey(
        Package,
        default=None,
        related_name='itineraries',
        on_delete=models.CASCADE
    )

    subtitle = models.CharField(max_length=255, default='')
    content = HTMLField()

    limit = models.PositiveIntegerField(default=0, blank=False, null=False)
    order = models.PositiveIntegerField(default=0, blank=False, null=False)

    active = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'itinerary'
        ordering = ['order']

    def __str__(self):
        return self.subtitle


class ItineraryImage(models.Model):

    alt = models.CharField(max_length=255, default='')

    slug = AutoSlugField(
        populate_from='alt',
        unique_with=['alt'],
        always_update=True
    )

    itinerary = models.ForeignKey(
        Itinerary,
        related_name='images',
        default=None,
        on_delete=models.CASCADE
    )

    image = ProcessedImageField(
        upload_to=path_and_rename,
        processors=[ResizeToFill(1000, 700)],
        format='JPEG',
        options={'quality': 100}
    )

    class Meta:
        db_table = 'itinerary_image'

    def __str__(self):
        return self.itinerary.subtitle


class ItineraryItems(models.Model):

    itinerary = models.ForeignKey(
        Itinerary,
        related_name='items',
        default=None,
        on_delete=models.CASCADE
    )

    types = models.CharField(
        max_length=100,
        choices=ITINERARY_CHOICES,
        default=''
    )

    text = models.CharField(max_length=255, default='')

    class Meta:
        db_table = 'itinerary_items'

    def __str__(self):
        return self.itinerary.subtitle


