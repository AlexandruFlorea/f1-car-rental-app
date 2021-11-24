from django.dispatch import receiver
from django.db.models.signals import post_save
from bookings.models import Booking
from utils.constants.booking_limits import CAR_BOOKING_LIMIT, TRACK_BOOKING_LIMIT


# for the signals to work, we need to define the ready method in apps.py, where we just import this signals module

# @receiver(post_save, sender=Booking)
# def car_availability_handler(instance, *args, **kwargs):
#     if instance.car.number_of_active_bookings >= CAR_BOOKING_LIMIT:
#         instance.car.available = False
#         instance.car.save()
#     else:
#         instance.car.available = True
#         instance.car.save()


@receiver(post_save, sender=Booking)
def track_availability_handler(instance, *args, **kwargs):
    if instance.track.number_of_active_bookings >= TRACK_BOOKING_LIMIT:
        instance.track.available = False
        instance.track.save()
    else:
        instance.track.available = True
        instance.track.save()
