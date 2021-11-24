from django.contrib import admin
from my_admin.admin import my_admin_site
from tracks.models import Track


@admin.register(Track, site=my_admin_site)  # register on the custom admin site
class TrackAdmin(admin.ModelAdmin):
    list_display = ('name', 'location', 'available', 'number_of_active_bookings', 'number_of_bookings')
