from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from bookings.models import Booking
from bookings.forms import BookingForm


def show_all_bookings(request):
    bookings = Booking.objects.all()
    paginator = Paginator(bookings, 5)

    page_obj = paginator.get_page(request.GET.get('page', 1))  # Objects on the page

    return render(request, 'bookings/bookings.html', {
        'page_obj': page_obj,  # sending just one page instead of the whole list
    })


def show_booking_details(request, booking_id):
    booking = get_object_or_404(Booking, pk=booking_id)

    return render(request, 'bookings/details.html', {
        'booking': booking
    })


def create_booking(request):
    # form = BookingForm(request.POST)
    # if form.is_valid():
    #     instance = form.save(commit=False)
    #     instance.save()

        return render(request, 'bookings/create_booking.html', {
        })
