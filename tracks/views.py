from django.shortcuts import render, get_object_or_404
from tracks.models import Track


def show_all_tracks(request):
    tracks = Track.objects.all()

    return render(request, 'tracks/tracks.html', {
        'tracks': tracks
    })


def show_track_details(request, track_id):
    track = get_object_or_404(Track, pk=track_id)

    return render(request, 'tracks/details.html', {
        'track': track
    })
