from django.db import models
from django.utils.text import slugify
from django.templatetags.static import static
import json
from datetime import datetime


class Track(models.Model):
    name = models.CharField(max_length=128, null=False)
    location = models.CharField(max_length=128, null=False)
    length = models.FloatField(default=0)
    available = models.BooleanField(default=True)
    available_from = models.DateTimeField(max_length=128, null=False)
    available_to = models.DateTimeField(max_length=128, null=False)

    def __str__(self):
        return f'Track object with ID: {self.name}'

    @property
    def image_urls(self):
        slug = slugify(self.name)

        return [static(f'tracks/images/{slug}.png')]

    @property
    def gallery_image_urls(self):
        with open('tracks/fixtures/tracks-gallery-images.json') as jsonfile:
            jsonobj = json.load(jsonfile)

        gallery = jsonobj[self.name]
        image_urls = []

        for image in gallery:
            image_urls += [static(image)]

        return image_urls
