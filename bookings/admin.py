from django.contrib import admin
from my_admin.admin import my_admin_site
from bookings.models import Booking


@admin.register(Booking, site=my_admin_site)  # register on the custom admin site
class BookingAdmin(admin.ModelAdmin):
    list_display = ['id','date_created', 'paid', 'user', 'car', 'track']
    search_fields = ['date_created', 'paid', 'user__email', 'car__name', 'track__name']

