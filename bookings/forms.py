from django import forms
from .models import Booking, Car, Track


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = [
            'start_date',
            'end_date',
            'car',
            'track',
            'user',
        ]
