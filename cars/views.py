from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.core.paginator import Paginator
from django.contrib import messages
from cars.models import Car
from cars.forms import FilterCarsForm
from tracks.models import Track
from utils.cart import Cart


def show_all_cars(request):
    form = FilterCarsForm(request.GET)
    form.is_valid()
    cars = form.apply_filters()

    paginator = Paginator(cars, 3)
    page_obj = paginator.get_page(request.GET.get('page', 1))  # Objects on the page

    return render(request, 'cars/cars.html', {
        'page_obj': page_obj,  # sending just one page instead of the whole list
        'form': form,
    })


def show_car_details(request, car_id):
    car = get_object_or_404(Car, pk=car_id)

    return render(request, 'cars/details.html', {
        'car': car,
    })


def add_car_to_cart(request, car_id):
    car = get_object_or_404(Car, pk=car_id)
    cart = Cart(request)
    cart.add_car(car_id)

    messages.info(request, f'{car.name} added to your booking.')

    booking = True  # to differentiate between normal view and booking process view
    tracks = Track.objects.all()
    paginator = Paginator(tracks, 4)
    page_obj = paginator.get_page(request.GET.get('page', 1))  # Objects on the page

    return render(request, 'tracks/tracks.html', {
        'page_obj': page_obj,
        'booking': booking,
    })


def remove_car_from_cart(request, car_id):
    get_object_or_404(Car, pk=car_id)
    cart = Cart(request)
    cart.remove_car()

    messages.success(request, 'Car removed.')

    return redirect(reverse('bookings:show-checkout'))
