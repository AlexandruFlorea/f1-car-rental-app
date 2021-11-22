from django.db import models
from django.conf import settings
from cars.models import Car
from tracks.models import Track
# from bookings.validators import validate_year, validate_time, validate_month, validate_day


class Booking(models.Model):
    date_created = models.DateTimeField(auto_now=True)
    date = models.DateField(null=True, blank=True)
    cost = models.FloatField(null=True, blank=True, default=0)
    # year = models.CharField(max_length=128, default=0)
    # month = models.CharField(max_length=128, default=0)
    # day = models.CharField(max_length=128, default=0)
    # time = models.CharField(max_length=128, default=0)
    finished = models.BooleanField(default=False)
    canceled = models.BooleanField(default=False)
    paid = models.BooleanField(default=False)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
                             related_name='bookings')
    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name='bookings')
    track = models.ForeignKey(Track, on_delete=models.CASCADE, related_name='bookings')

    class Meta:
        ordering = ['date_created']

    def __str__(self):
        status = 'Pending'
        if not self.paid and not self.finished and self.canceled:
            status = 'Canceled'
        elif (not self.paid and not self.finished and not self.canceled) or \
             (self.paid and not self.finished and not self.canceled):
            status = 'Active'
        elif self.paid and self.finished and not self.canceled:
            status = 'Finished'
        return f'{self.user.first_name} {self.user.last_name} rent a {self.car}, on {self.track} - ' \
               f'{self.track.location}, on {self.date} Status: {status}'

    @property
    def total_cost(self):
        return self.car.rate

    # def human_date(self):
    #     return self.date_created.strftime('%Y-%m-%d %H:%M:%S')
    # human_date.short_description = 'date_created'
    # human_date.admin_order_field = 'date_created'
