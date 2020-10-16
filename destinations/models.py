from django.db import models
from tinymce.models import HTMLField
from imagekit.models import ImageSpecField, ProcessedImageField
from imagekit.processors import ResizeToFill
from autoslug import AutoSlugField
from django.utils.timezone import now


class Country(models.Model):
    name = models.CharField(max_length=255)
    active = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'country'
        verbose_name_plural = 'Countries'

    def __str__(self):
        return self.name


class Destination(models.Model):
    title = models.CharField(max_length=255)
    slug = AutoSlugField(
        populate_from='title',
        unique_with=['title'],
        always_update=True
    )

    picture = models.ImageField(upload_to='images/destination/')

    thumbnail = ImageSpecField(
        source='picture',
        processors=[ResizeToFill(120, 50)],
        format='JPEG',
        options={'quality': 60}
    )

    original = ImageSpecField(
        source='picture',
        processors=[ResizeToFill(1500, 800)],
        format='JPEG',
        options={'quality': 80}
    )

    content = HTMLField()

    country = models.ForeignKey(
        Country,
        default=None,
        related_name='destinations',
        on_delete=models.CASCADE
    )

    active = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'destination'

    def __str__(self):
        return self.title


class Banner(models.Model):
    name = models.CharField(max_length=255)
    active = models.BooleanField(default=False)

    image = ProcessedImageField(
        upload_to='images/banner/',
        processors=[ResizeToFill(1600, 700)],
        format='JPEG',
        options={'quality': 100}
    )

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'banner'

    def __str__(self):
        return self.name
