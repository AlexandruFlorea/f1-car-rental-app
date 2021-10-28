from django.db import models
from django.conf import settings
from cars.models import Car
from tracks.models import Track


# Create your models here.
class Booking(models.Model):
    name = models.CharField(max_length=128, null=False)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    approved = models.BooleanField(default=False)
    finished = models.BooleanField(default=False)
    canceled = models.BooleanField(default=False)
    paid = models.BooleanField(default=False)
    total_price = models.FloatField(null=True, blank=True)
    rate = models.IntegerField(default=0)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
                             related_name='bookings')
    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name='bookings')
    track = models.ForeignKey(Track, on_delete=models.CASCADE, related_name='bookings')

    # class Meta:
    #     db_table = 'booking'  # overrides the database table name

    def __str__(self):
        status = 'Pending'
        if not self.approved and not self.paid and not self.finished and self.canceled:
            status = 'Canceled'
        elif (self.approved and not self.paid and not self.finished and not self.canceled) or \
             (self.approved and self.paid and not self.finished and not self.canceled):
            status = 'Active'
        elif self.approved and self.paid and self.finished and not self.canceled:
            status = 'Finished'
        return f'{self.user} rent a {self.car}, on {self.track} - {self.track.name} {self.start_date} - {self.end_date}, {status}'
