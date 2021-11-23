from django.dispatch import receiver
from django.db.models.signals import post_save
from bookings.models import Booking


@receiver(post_save, sender=Booking)
def car_available_handler(instance, *args, **kwargs):  # this method must be imported in apps.py
    if instance.car.number_of_active_bookings >= 5:
        instance.car.available = False
        instance.car.save()
    else:
        instance.car.available = True
        instance.car.save()
