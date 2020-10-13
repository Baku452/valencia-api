from django.db import models
from specialists.models import Specialist
from tinymce.models import HTMLField
from django.utils.html import mark_safe
from imagekit.models import ImageSpecField, ProcessedImageField
from autoslug import AutoSlugField
from imagekit.processors import ResizeToFill
from destinations.models import Destination


RATING_CHOICES = (
    ("1", "1"),
    ("2", "2"),
    ("3", "3"),
    ("4", "4"),
    ("5", "5"),
)

ACTIVITY_CHOICES = (
    (1, "Very HIgh"),
    (2, "HIgh"),
    (3, "Moderate"),
    (4, "Low"),
    (5, "Very Low"),
)

DAYS_CHOICES = (
    (1, 1),
    (2, 2),
    (3, 3),
    (4, 4),
    (5, 5),
    (6, 6),
    (7, 7),
    (8, 8),
    (9, 9),
    (10, 11),
    (12, 12),
    (13, 13),
    (14, 14),
    (15, 15),
    (16, 16),
    (17, 17),
    (18, 18),
    (19, 19),
    (20, 20),
    (21, 21),
    (22, 22),
    (23, 23),
    (24, 24),
    (25, 25),
    (26, 26),
    (27, 27),
    (28, 28),
    (29, 29),
    (30, 30),
    (31, 31),
    (32, 32),
    (33, 33),
    (34, 34),
    (35, 35),
    (36, 36),
    (37, 37),
    (38, 38),
)

MONTHS_CHOICES = (
    ("January", "January"),
    ("February", "February"),
    ("March", "March"),
    ("April", "April"),
    ("May", "May"),
    ("June", "June"),
    ("July", "July"),
    ("August", "August"),
    ("September", "September"),
    ("October", "October"),
    ("November", "November"),
    ("December", "December"),
)


class Month(models.Model):
    name = models.CharField(
        unique=True,
        max_length=255,
        choices=MONTHS_CHOICES,
        default=1
    )

    class Meta:
        db_table = 'month'
        ordering = ('id',)

    def __str__(self):
        return self.name


class PackageType(models.Model):
    title = models.CharField(max_length=255)
    active = models.BooleanField(default=False)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'package_type'

    def __str__(self):
        return self.title


class Experience(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(default='')

    package_type = models.ManyToManyField(PackageType)

    image = models.FileField(upload_to='images/experience/')

    thumbnail = ImageSpecField(
        source='image',
        processors=[ResizeToFill(340, 440)],
        format='JPEG',
        options={'quality': 98}
    )

    original = ImageSpecField(
        source='image',
        processors=[ResizeToFill(1400, 400)],
        format='JPEG',
        options={'quality': 98}
    )

    active = models.BooleanField(default=False)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'experience'

    def __str__(self):
        return self.title


class Package(models.Model):
    title = models.CharField(max_length=255, default='')
    summary = models.TextField(default='')
    slug = AutoSlugField(
        populate_from='title',
        unique_with=['title'],
        always_update=True
    )

    description = HTMLField()

    package_type = models.ManyToManyField(PackageType)
    experience = models.ManyToManyField(Experience)
    month = models.ManyToManyField(Month)

    specialist = models.ForeignKey(
        Specialist,
        related_name='specialist',
        default=None,
        on_delete=models.CASCADE,
    )

    destination = models.ForeignKey(
        Destination,
        default=None,
        on_delete=models.CASCADE,
    )

    activity = models.IntegerField(
        choices=ACTIVITY_CHOICES,
        default=1
    )

    days = models.IntegerField(
        choices=DAYS_CHOICES,
        default=1
    )

    physical_difficulty = models.CharField(
        max_length=2,
        choices=RATING_CHOICES,
        default='1'
    )

    cultural_rating = models.CharField(
        max_length=2,
        choices=RATING_CHOICES,
        default='1'
    )

    wildlife_expectation = models.CharField(
        max_length=2,
        choices=RATING_CHOICES,
        default='1'
    )

    thumbnail = ProcessedImageField(
        upload_to='images/packages-thumbnail/',
        processors=[ResizeToFill(280, 190)],
        format='JPEG',
        options={'quality': 100}
    )

    published = models.BooleanField(default=False)
    is_home = models.BooleanField(default=False)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'package'

    def __str__(self):
        return self.title


class PackageImage(models.Model):
    package = models.ForeignKey(
        Package,
        related_name='images',
        default=None,
        on_delete=models.CASCADE
    )
    image = models.FileField(upload_to='images/package/')

    original = ImageSpecField(
        source='image',
        processors=[ResizeToFill(1400, 500)],
        format='JPEG',
        options={'quality': 100}
    )

    alt = models.CharField(max_length=255, default='')

    class Meta:
        db_table = 'package_image'

    def __str__(self):
        return self.package.title

    def image_tag(self):
        return mark_safe('<img src="/media/%s" width="150" height="150" />' % self.image)




