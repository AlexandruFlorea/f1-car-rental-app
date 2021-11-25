from django.db import models
from django.conf import settings
import datetime
from cars.models import Car
from tracks.models import Track


class Booking(models.Model):
    booking_number = models.CharField(max_length=9, blank=False, default=0)
    date_created = models.DateTimeField(auto_now_add=True)
    date = models.DateField(null=True, blank=True)
    cost = models.FloatField(null=True, blank=True, default=0)
    finished = models.BooleanField(default=False)
    canceled = models.BooleanField(default=False)
    paid = models.BooleanField(default=False)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
                             related_name='bookings')
    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name='bookings')
    track = models.ForeignKey(Track, on_delete=models.CASCADE, related_name='bookings')

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return str(self.booking_number)

    def save(self, *args, **kwargs):
        today = datetime.date.today()
        today_string = today.strftime('%y%m%d')
        next_booking_number = '001'
        last_booking = Booking.objects.filter(booking_number__startswith=today_string).order_by('booking_number').last()
        if last_booking:
            last_booking_number = int(last_booking.booking_number[6:])
            next_booking_number = '{0:03d}'.format(last_booking_number + 1)
        self.booking_number = today_string + next_booking_number
        super(Booking, self).save(*args, **kwargs)

    @property
    def status(self):
        status = 'Pending'
        if not self.paid and not self.finished and self.canceled:
            status = 'Canceled'
        elif (not self.paid and not self.finished and not self.canceled) or \
             (self.paid and not self.finished and not self.canceled):
            status = 'Active'
        elif self.paid and self.finished and not self.canceled:
            status = 'Finished'

        return status

    # @property
    # def total_cost(self):
    #     return self.car.rate

    # def human_date(self):
    #     return self.date_created.strftime('%Y-%m-%d %H:%M:%S')
    # human_date.short_description = 'date_created'
    # human_date.admin_order_field = 'date_created'
