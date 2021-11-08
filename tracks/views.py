from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.core.paginator import Paginator
from django.contrib import messages
from tracks.models import Track
from utils.cart import Cart


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


def add_track_to_cart(request, track_id):
    track = get_object_or_404(Track, pk=track_id)
    cart = Cart(request)
    cart.add(track_id)

    messages.info(request, f'{track.name} added to your booking.')

    print(request.session['cart'])
    return redirect(reverse('bookings:show-checkout'))


def remove_track_from_cart(request, track_id):
    get_object_or_404(Track, pk=track_id)
    cart = Cart(request)
    cart.remove(track_id)

    messages.success(request, 'Item removed.')

    return redirect(reverse('bookings:show-checkout'))
