from django.db import models
from django.conf import settings
from datetime import datetime
from cars.models import Car
from tracks.models import Track


class Booking(models.Model):
    name = models.CharField(max_length=128, null=False)
    date_created = models.DateTimeField(auto_now=True)
    year = models.CharField(max_length=128, default=0)
    month = models.CharField(max_length=128, default=0)
    day = models.CharField(max_length=128, default=0)
    time = models.CharField(max_length=128, default=0)
    finished = models.BooleanField(default=False)
    canceled = models.BooleanField(default=False)
    paid = models.BooleanField(default=False)
    total_price = models.FloatField(null=True, blank=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
                             related_name='bookings')
    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name='bookings')
    track = models.ForeignKey(Track, on_delete=models.CASCADE, related_name='bookings')

    def __str__(self):
        status = 'Pending'
        if not self.paid and not self.finished and self.canceled:
            status = 'Canceled'
        elif (not self.paid and not self.finished and not self.canceled) or \
             (self.paid and not self.finished and not self.canceled):
            status = 'Active'
        elif self.paid and self.finished and not self.canceled:
            status = 'Finished'
        return f'{self.user.first_name} {self.user.last_name} rent a {self.car}, on {self.track} - {self.track.location}, on {self.date_created} Status: {status}'
