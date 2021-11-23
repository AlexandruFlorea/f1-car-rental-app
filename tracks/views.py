from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.core.paginator import Paginator
from tracks.models import Track


def show_all_tracks(request):
    tracks = Track.objects.all()
    paginator = Paginator(tracks, 4)

    page_obj = paginator.get_page(request.GET.get('page', 1))  # Objects on the page

    return render(request, 'tracks/tracks.html', {
        'page_obj': page_obj,  # sending just one page instead of the whole list
    })


def show_track_details(request, track_id):
    track = get_object_or_404(Track, pk=track_id)

    return render(request, 'tracks/details.html', {
        'track': track,
    })
