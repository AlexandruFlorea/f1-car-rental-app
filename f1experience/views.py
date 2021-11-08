from django.shortcuts import render
from bookings.models import Booking


def homepage_view(request):
    title = 'Formula 1 Experience'
    bookings = Booking.objects.all()[:5]

    return render(request, 'homepage.html', {
        'title': title,
        'bookings': bookings,
    })
