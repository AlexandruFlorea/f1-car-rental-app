from django.shortcuts import render, get_object_or_404
from cars.models import Car


def show_all_cars(request):
    cars = Car.objects.all()

    return render(request, 'cars/cars.html', {
        'cars': cars
    })


def show_car_details(request, car_id):
    car = get_object_or_404(Car, pk=car_id)

    return render(request, 'cars/details.html', {
        'car': car
    })
