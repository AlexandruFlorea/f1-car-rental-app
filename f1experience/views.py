from django.shortcuts import render, redirect, reverse
from django.db.models import Q
from bookings.models import Booking
from cars.models import Car
from tracks.models import Track
from .random_facts import get_fact


def homepage_view(request):
    title = 'Formula 1 Experience'
    latest_bookings = Booking.objects.all().order_by('-id')[:5]
    all_cars = Car.objects.all()
    car_list = [
        {
            'car': car.name,
            'car_bookings': car.bookings.count(),
        }
        for car in all_cars
    ]
    car_list_sorted = sorted(car_list, key=lambda car: car['car_bookings'], reverse=True)[:5]
    dict_values = []
    for item in car_list_sorted:
        key = item.get('car')
        value = item.get('car_bookings')
        dict_values.append(tuple((key, value)))

    top_5 = dict(dict_values)

    random_fact = get_fact()

    return render(request, 'homepage.html', {
        'title': title,
        'latest_bookings': latest_bookings,
        'top_5': top_5,
        'random_fact': random_fact,
    })


def search_site(request):
    if request.method == 'POST':
        query = request.POST.get('q')

        if query:
            cars = Car.objects.filter(Q(name__icontains=query)).distinct()
            tracks = Track.objects.filter(Q(name__icontains=query) | Q(location__icontains=query)).distinct()
            if request.user.is_authenticated:
                bookings = request.user.bookings.filter(
                    Q(date_created__icontains=query) | Q(user__email__icontains=query) | Q(car__name__icontains=query) |
                    Q(track__name__icontains=query) | Q(track__location__icontains=query)
                    ).distinct()

                return render(request, 'search.html', {
                    'query': query,
                    'cars': cars,
                    'tracks': tracks,
                    'bookings': bookings,
                })

            return render(request, 'search.html', {
                'query': query,
                'cars': cars,
                'tracks': tracks,
            })

    return redirect(reverse('homepage'))
