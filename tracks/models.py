import json
from django.db import models
from django.db.models import Q
from django.utils import timezone
from django.templatetags.static import static


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

    @property
    def number_of_bookings(self):
        bookings = Track.objects.filter(bookings__track=self).count()

        return bookings

    @property
    def number_of_active_bookings(self):
        bookings = Track.objects.filter(Q(bookings__track=self), Q(bookings__canceled=False)).count()

        return bookings
