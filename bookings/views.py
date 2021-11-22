from django.shortcuts import render, get_object_or_404, redirect, reverse, Http404, HttpResponseRedirect
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from bookings.models import Booking
from bookings.forms import BookingDateForm
from cars.models import Car
from tracks.models import Track


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
    cars = Car.objects.all()
    paginator = Paginator(cars, 4)  # Objects on the page
    page_obj = paginator.get_page(request.GET.get('page', 1))

    return render(request, 'cars/cars.html', {
        'page_obj': page_obj,
        'booking': booking,
    })


@login_required(login_url='/users/login/')
def create_booking_old(request):
#     submitted = False
#     if request.method == 'POST':
#         form = BookingForm(request.POST)
#         if form.is_valid():
#             form = form.save(commit=False)
#             form.user = request.user
#             print(request.POST.get('car'))
#             form.save()
#             messages.success(request, 'Booking created successfully!')
#
#             return HttpResponseRedirect('/bookings/create_old?submitted=True')
#     else:
#         form = BookingForm()
#         if 'submitted' in request.GET:
#             submitted = True
#
#     return render(request, 'bookings/create_booking_old.html', {
#         'form': form,
#         'submitted': submitted,
#
#     })
    pass


# @login_required(login_url='/users/login/')
# def show_checkout(request):
#     cart = request.session.get('cart', {})  # get cart or create an empty one
#     car = Car.objects.filter(id__in=cart.values()).first()
#     track = Track.objects.filter(id__in=cart.values()).first()
#     date = track.race_day
#     cost = car.rate
#     user = request.user
#
#     if request.method == 'GET':
#         form = BookingDateForm(user, car, track, date, cost,)
#     else:
#         form = BookingDateForm(user, car, track, date, cost, request.POST)
#         if form.is_valid():
#             form.user = user
#             form.car = car
#             form.track = track
#             form.date = date
#             form.cost = cost
#             form.save()
#
#             messages.success(request, 'Booking created successfully!')
#             request.session['cart'] = {}
#
#             return redirect('/')
#
#         else:
#             print('Form not valid!!!!!!!')
#
#
#             return redirect('/')
#
#     return render(request, 'bookings/checkout.html', {
#         'car': car,
#         'track': track,
#         'cart': cart,
#         'form': form,
#     })


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

        return redirect('/')

    return render(request, 'bookings/checkout.html', {
        'car': car,
        'track': track,
    })
