from django.shortcuts import render, get_object_or_404, redirect, reverse, Http404, HttpResponseRedirect
from django.core.paginator import Paginator
from django.conf import settings
from django.contrib.auth.decorators import login_required
from .models import Booking, Car, Track
from .forms import BookingForm



@login_required
def show_all_bookings(request):
    bookings = request.user.bookings.all()
    paginator = Paginator(bookings, 15)

    page_obj = paginator.get_page(request.GET.get('page', 1))  # Objects on the page

    return render(request, 'bookings/bookings.html', {
        'page_obj': page_obj,  # sending just one page instead of the whole list
    })


@login_required
def show_booking_details(request, booking_id):
    booking = get_object_or_404(Booking, pk=booking_id)


    if booking.user.id != request.user.id:
        raise Http404('Booking not available.')

    return render(request, 'bookings/details.html', {
        'booking': booking
    })


@login_required
def create_booking(request):
    submitted = False
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user
            form.save()

            return HttpResponseRedirect('/bookings/create?submitted=True')
    else:
        form = BookingForm()
        if 'submitted' in request.GET:
            submitted = True

    return render(request, 'bookings/create_booking.html', {
        'form': form,
        'submitted': submitted,

    })
