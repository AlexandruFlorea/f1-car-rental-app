from django.urls import path
from bookings.views import show_all_bookings, show_booking_details, create_booking, \
    show_checkout, cancel_booking, remove_car_from_cart, remove_track_from_cart, \
    add_car_to_cart, add_track_to_cart


app_name = 'bookings'

urlpatterns = [
    path('', show_all_bookings, name='all'),
    path('create/', create_booking, name='create'),
    path('<int:booking_id>/', show_booking_details, name='details'),
    path('<int:booking_id>/cancel/', cancel_booking, name='cancel_booking'),
    path('checkout/', show_checkout, name='show_checkout'),
    path('<int:car_id>/remove_car_from_cart/', remove_car_from_cart, name='remove_car_from_cart'),
    path('<int:track_id>/remove_track_from_cart/', remove_track_from_cart, name='remove_track_from_cart'),
    path('<int:car_id>/add_car_to_cart/', add_car_to_cart, name='add_car_to_cart'),
    path('<int:track_id>/add_track_to_cart/', add_track_to_cart, name='add_track_to_cart'),

]
