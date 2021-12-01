from django.core.management.base import BaseCommand
from bookings.models import Booking


class Command(BaseCommand):
    help = 'Update booking number for backdated orders.'

    def handle(self, *args, **options):
        bookings = Booking.objects.all().order_by('id')

        print(f'Updating a total of {len(bookings)} bookings.')

        index = 135
        for booking in bookings:
            booking.booking_number = f'{booking.date_created.strftime("%y%m%d")}{index}'
            index += 1
            booking.save()
