from django.core.management.base import BaseCommand
from tracks.models import Track
from utils.constants.booking_limits import TRACK_BOOKING_LIMIT


class Command(BaseCommand):
    help = 'Mark track as available'

    def handle(self, *args, **kwargs):
        tracks = Track.objects.all()

        print(f'Verifying a total of {len(tracks)} tracks.')

        for track in tracks:
            if track.number_of_active_bookings < TRACK_BOOKING_LIMIT:
                track.available=True
                track.save()
            else:
                track.available=False
                track.save()
