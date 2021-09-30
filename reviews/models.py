from django.db import models

# Create your models here.

RATING_CHOICES = (
    (0, "0"),
    (1, "1"),
    (2, "2"),
    (3, "3"),
    (4, "4"),
    (5, "5"),
)


class TripadvisorReviews(models.Model):
    title = models.CharField(max_length=255, default='')
    name = models.CharField(max_length=255, default='')
    content = models.TextField(blank=True, null=True)
    rating = models.IntegerField(default=0, choices=RATING_CHOICES)
    published = models.BooleanField(default=False)
    url = models.CharField(max_length=255, default='')
    date = models.DateField()
    class Meta:
        verbose_name_plural = "Trip Advisor Reviews"
    def __str__(self):
        return self.title
