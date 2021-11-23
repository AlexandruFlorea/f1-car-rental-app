from django.core.management.base import BaseCommand
from bookings.models import Booking


class Command(BaseCommand):
    help = 'Assign booking cost to backdated orders.'

    def handle(self, *args, **options):
        bookings = Booking.objects.filter(cost=0)

        print(f'Updating a total of {len(bookings)} bookings.')

        for booking in bookings:
            booking.cost = booking.car.rate
            booking.save()
