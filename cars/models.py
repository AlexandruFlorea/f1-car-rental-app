from django.db import models
from django.utils.text import slugify
from django.templatetags.static import static
from django.core import serializers
import json


# Create your models here.
class Car(models.Model):
    name = models.CharField(max_length=128, unique=True, null=False)
    power_unit = models.CharField(max_length=128, unique=False, null=False)
    races_won = models.IntegerField(default=0)
    handling = models.CharField(max_length=128, null=False)
    price_per_lap = models.IntegerField(default=1000)

    def __str__(self):
        return f'Car object ID = {self.id}'

    @property
    def image_urls(self):
        slug = slugify(self.name)

        return [static(f'cars/images/small/{slug}.png')]

    @property
    def gallery_image_urls(self):
        with open('cars/fixtures/car-gallery-images.json') as jsonfile:
            jsonobj = json.load(jsonfile)

        gallery = jsonobj[self.name]
        image_urls = []
        print(image_urls)
        for image in gallery:
            image_urls += [static(image)]

            return image_urls
        return image_urls
