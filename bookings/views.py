from django.shortcuts import render, get_object_or_404, redirect, Http404, reverse
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from bookings.models import Booking
from utils.cart import Cart
from cars.models import Car
from tracks.models import Track
from utils.constants.booking_limits import CAR_BOOKING_LIMIT


@login_required
def show_all_bookings(request):
    if request.method == 'POST':
        query = request.POST.get('q')
        if query:
            lookups = (Q(car__name__icontains=query) | Q(track__name__icontains=query) | Q(user__email__icontains=query)
                       | Q(track__location__icontains=query) | Q(date_created__icontains=query))

            bookings = request.user.bookings.filter(lookups).distinct()
            paginator = Paginator(bookings, 15)  # Objects on the page
            page_obj = paginator.get_page(request.GET.get('page', 1))

            return render(request, 'bookings/bookings.html', {
                'page_obj': page_obj,
            })

    bookings = request.user.bookings.all()
    paginator = Paginator(bookings, 15)  # Objects on the page
    page_obj = paginator.get_page(request.GET.get('page', 1))  # sending just one page instead of the whole list

    return render(request, 'bookings/bookings.html', {
        'page_obj': page_obj,
    })


@login_required(login_url='/users/login/')
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
    tracks = Track.objects.all()
    paginator = Paginator(tracks, 4)  # Objects on the page
    page_obj = paginator.get_page(request.GET.get('page', 1))

    return render(request, 'tracks/tracks.html', {
        'page_obj': page_obj,
        'booking': booking,
    })


def add_track_to_cart(request, track_id):
    track = get_object_or_404(Track, pk=track_id)
    cart = Cart(request)
    cart.add_track(track_id)
    messages.info(request, f'{track.name} added to your booking.')

    booking = True  # to differentiate between normal view and booking process view
    #  verify car availability
    cars = Car.objects.all()
    available_cars = []
    for car in cars:
        bookings_on_track = Booking.objects.filter(Q(track=track), Q(car=car), Q(canceled=False)).count()
        if bookings_on_track < CAR_BOOKING_LIMIT:
            available_cars.append(car)

    paginator = Paginator(cars, 3)
    page_obj = paginator.get_page(request.GET.get('page', 1))  # Objects on the page

    return render(request, 'cars/cars.html', {
        'page_obj': page_obj,
        'booking': booking,
        'available_cars': available_cars,
    })


def remove_track_from_cart(request, track_id):
    get_object_or_404(Track, pk=track_id)
    cart = Cart(request)
    cart.remove_track()

    messages.success(request, 'Track removed.')

    return redirect(reverse('bookings:show_checkout'))


def add_car_to_cart(request, car_id):
    car = get_object_or_404(Car, pk=car_id)
    cart = Cart(request)
    cart.add_car(car_id)

    messages.info(request, f'{car.name} added to your booking.')

    return redirect(reverse('bookings:show_checkout'))


def remove_car_from_cart(request, car_id):
    get_object_or_404(Car, pk=car_id)
    cart = Cart(request)
    cart.remove_car()

    messages.success(request, 'Car removed.')

    return redirect(reverse('bookings:show_checkout'))


@login_required(login_url='/users/login/')
def show_checkout(request):
    cart = request.session.get('cart', {})  # get cart or create an empty one
    car = Car.objects.filter(id__in=cart.values()).first()
    track = Track.objects.filter(id__in=cart.values()).first()
    user = request.user

    if request.method == 'POST':
        current_booking = Booking(car=car, track=track, user=user, date=track.race_day, cost=car.rate)
        current_booking.save()

        messages.success(request, 'Booking created successfully!')
        request.session['cart'] = {}

        # # Control car availability
        # if car.number_of_bookings >= 5:
        #     car.available = False
        #     car.save()

        return redirect('/')

    return render(request, 'bookings/checkout.html', {
        'car': car,
        'track': track,
    })


@login_required(login_url='/users/login/')
def cancel_booking(request, booking_id):
    booking = get_object_or_404(Booking, pk=booking_id)
    booking.canceled = True
    booking.save()

    messages.success(request, 'Booking cancelled successfully!')

    # # Control car availability
    # if booking.car.number_of_bookings < 5:
    #     booking.car.available = True
    #     booking.car.save()

    return redirect(reverse('bookings:all'))
