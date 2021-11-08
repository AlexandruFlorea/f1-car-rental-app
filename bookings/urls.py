from django.urls import path
from bookings.views import show_all_bookings, create_booking_old, show_booking_details, \
    search_bookings, create_booking, show_checkout, booking_date
from cars.views import remove_car_from_cart
from tracks.views import remove_track_from_cart


app_name = 'bookings'

urlpatterns = [
    path('', show_all_bookings, name='all'),
    path('create_old/', create_booking_old, name='create-old'),
    path('create/', create_booking, name='create'),
    path('<int:booking_id>/', show_booking_details, name='details'),
    path('search_bookings/', search_bookings, name='search-bookings'),
    path('checkout/', show_checkout, name='show-checkout'),
    path('<int:car_id>/remove_car_from_cart/', remove_car_from_cart, name='remove_car_from_cart'),
    path('<int:track_id>/remove_track_from_cart/', remove_track_from_cart, name='remove_track_from_cart'),
    path('<int:track_id>/remove_track_from_cart/', remove_track_from_cart, name='remove_track_from_cart'),

]
