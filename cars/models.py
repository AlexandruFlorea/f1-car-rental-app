from django.db import models
from django.utils.text import slugify
from django.templatetags.static import static
from django.conf import settings
import json


# Create your models here.
class Category(models.Model):
    class Meta:
        verbose_name_plural = 'categories'

    name = models.CharField(max_length=128, null=False)

    def __str__(self):
        return self.name


class Car(models.Model):
    name = models.CharField(max_length=128, unique=True, null=False)
    power_unit = models.CharField(max_length=128, unique=False, null=False)
    races_won = models.IntegerField(default=0)
    handling = models.CharField(max_length=128, null=False)
    rate = models.IntegerField(default=1000)
    available = models.BooleanField(default=True)
    color = models.CharField(max_length=24, null=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, related_name='cars', null=True, default=None)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, related_name='cars', null=True, default=None)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        ordering = ['name']

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

        for image in gallery:
            image_urls += [static(image)]

        return image_urls

    @property
    def number_of_bookings(self):
        queryset = Car.objects.filter(booking__car__name=self).count()

        return queryset

    # @property
    # def get_last_booking(self):
    #     latest_booking = Booking.objects.filter(car=self).order_by('-date').first()
    #
    #     return latest_booking
