from django.core.management.base import BaseCommand
from bookings.models import Booking


class Command(BaseCommand):
    help = 'Assign booking date to backdated orders.'

    def handle(self, *args, **options):
        bookings = Booking.objects.filter(date=None)

        print(f'Updating a total of {len(bookings)} bookings.')

        for booking in bookings:
            booking.date = booking.track.race_day
            booking.save()
