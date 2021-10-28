from django.urls import path
from bookings.views import show_all_bookings, create_booking


app_name = 'bookings'

urlpatterns = [
    path('', show_all_bookings, name='all'),
    path('create/', create_booking, name = 'create')
]
