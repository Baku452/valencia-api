from django.db import models
from tinymce.models import HTMLField
from packages.models import Package
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill

ITINERARY_CHOICES = (
    ("Meals Included", "Meals Included"),
    ("Accommodations", "Accommodations"),
)


# Create your models here.
class Itinerary(models.Model):

    package = models.ForeignKey(
        Package,
        default=None,
        related_name='itineraries',
        on_delete=models.CASCADE
    )

    subtitle = models.CharField(max_length=255, default='')
    content = HTMLField()
    active = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'itinerary'

    def __str__(self):
        return self.subtitle


class ItineraryImage(models.Model):

    itinerary = models.ForeignKey(
        Itinerary,
        related_name='images',
        default=None,
        on_delete=models.CASCADE
    )

    image = ProcessedImageField(
        upload_to='images/itinerary/',
        processors=[ResizeToFill(1000, 700)],
        format='JPEG',
        options={'quality': 100}
    )

    alt = models.CharField(max_length=255, default='')

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


