from django.urls import path
from bookings.views import show_all_bookings, create_booking, show_booking_details


app_name = 'bookings'

urlpatterns = [
    path('', show_all_bookings, name='all'),
    path('create/', create_booking, name = 'create'),
    path('<int:booking_id>/', show_booking_details, name = 'details'),
]
