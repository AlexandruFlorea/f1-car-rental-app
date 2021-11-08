from django import forms
from .models import Booking
from utils.constants.time_select import AVAILABLE_HOURS


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        widgets = {
            'user': forms.HiddenInput(),
            'date': forms.SelectDateWidget,
            'time': forms.Select(choices=AVAILABLE_HOURS)

        }
        fields = [
            'car',
            'track',
            'date',
            'time',
        ]


class BookingDateForm(forms.Form):
    year = forms.ChoiceField(choices=())
    month = forms.ChoiceField(choices=())
    day = forms.ChoiceField(choices=())
    time = forms.ChoiceField(choices=())
