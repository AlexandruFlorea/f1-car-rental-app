from django.shortcuts import render, get_object_or_404, redirect, reverse, Http404, HttpResponseRedirect
from django.core.paginator import Paginator
from django.conf import settings
from django.contrib.auth.decorators import login_required
from bookings.models import Booking
from bookings.forms import BookingForm, BookingDateForm
from cars.models import Car
from tracks.models import Track
from utils.cart import Cart


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
        'booking': booking,
    })


@login_required(login_url='/users/login/')
def create_booking(request):
    booking = True
    cars = Car.objects.all()
    paginator = Paginator(cars, 4)
    page_obj = paginator.get_page(request.GET.get('page', 1))  # Objects on the page

    return render(request, 'cars/cars.html', {
        'page_obj': page_obj,
        'booking': booking,
    })


@login_required(login_url='/users/login/')
def create_booking_old(request):
    submitted = False
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user
            form.save()

            return HttpResponseRedirect('/bookings/create_old?submitted=True')
    else:
        form = BookingForm()
        if 'submitted' in request.GET:
            submitted = True

    return render(request, 'bookings/create_booking_old.html', {
        'form': form,
        'submitted': submitted,

    })


def search_bookings(request):

    return render(request, 'bookings/search_bookings.html', {})


@login_required(login_url='/users/login/')
def show_checkout(request):
    cart = request.session.get('cart', {})
    cars = Car.objects.filter(id__in=cart.keys())
    tracks = Track.objects.filter(id__in=cart.keys())

    # cart_items = []
    car_items = [
        {
            'car': car,
            'total': '%.2f' % float(car.rate)
        }
        for car in cars
    ]

    track_items = [
        {
            'track': track,
        }
        for track in tracks
    ]

    # cart_items.extend(car_item)
    # cart_items.extend(track_item)

    return render(request, 'bookings/checkout.html', {
        'car_items': car_items,
        'track_items': track_items,
        'cart': cart,
    })


def booking_date(request):
    form = BookingDateForm(request.POST)
    if form.is_valid():
        form = form.save(commit=False)
        form.user = request.user
        form.save()

    return redirect(request, 'bookings/checkout.html', {
        'form': form,

    })
