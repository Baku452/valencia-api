from django.db import models
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill
from datetime import date

class Specialist(models.Model):
    fullname = models.CharField(max_length=255, default='')
    email = models.EmailField(max_length=255, default='')
    thumbnail = ProcessedImageField(
        upload_to='specialist-thumbnail',
        processors=[ResizeToFill(200, 200)],
        format='JPEG',
        options={'quality': 100}
    )
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'specialist'

    def __str__(self):
        return self.fullname


class Newsletter(models.Model):
    first_name = models.CharField(max_length=255, default='')
    last_name = models.CharField(max_length=255, default='')
    email = models.EmailField(max_length=255, default='')

    package_type = models.ManyToManyField(to='packages.PackageType')

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'newsletter'

    def __str__(self):
        return self.first_name


class ContactUs(models.Model):
    first_name = models.CharField(max_length=255, default='')
    last_name = models.CharField(max_length=255, default='')
    email = models.EmailField(max_length=255, default='')
    country_residence = models.CharField(max_length=255, default='')
    destination_interest = models.CharField(max_length=255, default='')
    number = models.CharField(max_length=255, default='')
    message = models.TextField(max_length=999, default='')
    is_newsletter = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'contact_us'

    def __str__(self):
        return self.first_name

class ContactUsB2C(models.Model):
    first_name = models.CharField(max_length=255, default='')
    last_name = models.CharField(max_length=255, default='')
    email = models.EmailField(max_length=255, default='')
    country = models.CharField(max_length=255, default='')
    state = models.CharField(max_length=255, default='')
    city = models.CharField(max_length=255, default='')
    number = models.CharField(max_length=255, default='')
    package = models.CharField(max_length=255, default='')
    message = models.TextField(max_length=999, default='')
    is_newsletter = models.BooleanField(default=False)
    is_promo = models.BooleanField(default=False)
    url = models.CharField(max_length=255, default='')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'contact_usB2C'

    def __str__(self):
        return self.first_name


class ContactUsB2B(models.Model):
    first_name = models.CharField(max_length=255, default='')
    last_name = models.CharField(max_length=255, default='')
    email = models.EmailField(max_length=255, default='')
    number = models.CharField(max_length=255, default='')
    company = models.CharField(max_length=255, default='')
    package = models.CharField(max_length=255, default='')
    message = models.TextField(max_length=999, default='')
    is_promo = models.BooleanField(default=False)
    url = models.CharField(max_length=255, default='')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'contact_usB2B'

    def __str__(self):
        return self.company


class TailorForm(models.Model):
    first_name = models.CharField(max_length=255, default='')
    last_name = models.CharField(max_length=255, default='')
    email = models.EmailField(max_length=255, default='')
    number = models.CharField(max_length=255, default='')  
    destination_interest = models.CharField(max_length=255, default='')
    accommodation = models.CharField(max_length=255, default='')
    departureDate = models.DateField(default = date.today)
    lengthStay = models.CharField(max_length=255, default='')
    adults = models.IntegerField(default=0)
    children = models.IntegerField(default=0)
    internationalFlight = models.CharField(max_length=255, default='')
    budget = models.CharField(max_length=255, default='')
    trip_type = models.CharField(max_length=255, default='')
    hear_about = models.CharField(max_length=255, default='')
    message = models.TextField(max_length=999, default='')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'tailorForm'

    def __str__(self):
        return self.first_name
