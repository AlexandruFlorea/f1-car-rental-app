from django.core.management.base import BaseCommand
from tracks.models import Track


class Command(BaseCommand):
    help = 'Mark track as available'

    def handle(self, *args, **kwargs):
        tracks = Track.objects.filter(available=False)

        print(f'Updating a total of {len(tracks)} tracks.')

        for track in tracks:
            track.available=True
            track.save()
