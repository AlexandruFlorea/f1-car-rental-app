from django.db import models
from django.utils import timezone
from django.templatetags.static import static
import json


class Track(models.Model):
    name = models.CharField(max_length=128, null=False)
    location = models.CharField(max_length=128, null=False)
    length = models.FloatField(default=0)
    available = models.BooleanField(default=True)
    race_day = models.DateField(null=True, blank=True, default=timezone.now)
    weather_code = models.CharField(max_length=128, null=True, default='iasi_romania_675810')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        ordering = ['id']

    @property
    def first_image_url(self):

        return [static(f'tracks/images/{self.name}.png')]

    @property
    def gallery_image_urls(self):
        with open('tracks/fixtures/tracks-gallery-images.json') as jsonfile:
            jsonobj = json.load(jsonfile)

        gallery = jsonobj[self.name]
        image_urls = []

        for image in gallery:
            image_urls += [static(image)]

        return image_urls


# class TrackAvailableDates(models.Model):
#     track = models.OneToOneField(Track, on_delete=models.CASCADE, related_name='dates')
#     year = models.CharField(max_length=128, default=0, null=True, blank=True)
#     month = models.CharField(max_length=128, default=0)
#     day = models.CharField(max_length=128, default=0, null=True, blank=True)
#     time = models.CharField(max_length=128, default=0, null=True, blank=True)
#
#     def __str__(self):
#         return f'{self.year}-{self.month}-{self.day}'
