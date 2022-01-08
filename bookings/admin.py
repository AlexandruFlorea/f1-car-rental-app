import csv
from django.contrib import admin
from django.shortcuts import HttpResponse
from my_admin.admin import my_admin_site
from bookings.models import Booking
from cars.models import Car


@admin.register(Booking, site=my_admin_site)  # register on the custom admin site
class BookingAdmin(admin.ModelAdmin):
    @admin.action(description='Generate Excel report')
    def generate_report(self, request, queryset):
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="my_bookings.csv"'
        bookings = queryset
        header = ['Booking number', 'Track', 'Car', 'Booked date', 'User email']
        writer = csv.writer(response)
        writer.writerow(header)
        for booking in bookings:
            writer.writerow([booking.booking_number, booking.track, booking.car, booking.date, booking.user])

        return response

    @admin.action(description='Cancel bookings')
    def cancel_bookings(self, request, queryset):
        bookings = queryset
        for booking in bookings:
            booking.canceled = True
            booking.save()

    list_display = ['booking_number', 'user', 'car', 'track', 'date', 'cost', 'date_created', 'paid', 'canceled']
    search_fields = ['date_created', 'paid', 'user__email', 'car__name', 'track__name', 'booking_number']
    list_filter = ['paid', 'date_created', 'car', 'track']
    actions = [generate_report, cancel_bookings, ]

    def get_queryset(self, request):
        queryset = super().get_queryset(request)  # accesses the parent queryset
        if request.user.is_superuser:
            return queryset

        return queryset.filter(car__owner=request.user)  # can access bookings for owned cars only

    def formfield_for_foreignkey(self, db_field, request, **kwargs):  # control access to items linked via FK
        if db_field.name == 'car' and not request.user.is_superuser:
            kwargs['queryset'] = Car.objects.filter(owner=request.user)  # limit list options to owned cars

        return super().formfield_for_foreignkey(db_field, request, **kwargs)
