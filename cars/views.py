from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.core.paginator import Paginator
from cars.models import Car
from cars.forms import FilterCarsForm


def show_all_cars(request):
    form = FilterCarsForm(request.GET)
    form.is_valid()
    cars = form.apply_filters()

    paginator = Paginator(cars, 4)
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
