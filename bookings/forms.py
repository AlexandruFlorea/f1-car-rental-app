from django import forms
from bookings.models import Booking
from tracks.models import TrackAvailableDates
from utils.constants.booking_date_select import AVAILABLE_HOURS, AVAILABLE_MONTHS, \
    AVAILABLE_YEARS, AVAILABLE_DAYS


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        widgets = {
            'user': forms.HiddenInput(),
            'year': forms.Select(choices=AVAILABLE_YEARS),
            'month': forms.Select(choices=AVAILABLE_MONTHS),
            'day': forms.Select(choices=AVAILABLE_DAYS),
            'time': forms.Select(choices=AVAILABLE_HOURS)

        }
        fields = [
            'car',
            'track',
            'year',
            'month',
            'day',
            'time',
        ]


# class BookingDateForm(forms.Form):
#     year = forms.ChoiceField(choices=AVAILABLE_HOURS)
#     month = forms.ChoiceField(choices=(AVAILABLE_HOURS))
#     day = forms.ChoiceField(choices=(AVAILABLE_HOURS))
#     hour = forms.ChoiceField(choices=(AVAILABLE_HOURS))


class BookingDateForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['year', 'month', 'day', 'time', 'user', 'car', 'track' ]
        widgets = {
            'year': forms.Select(choices=AVAILABLE_YEARS),
            'month': forms.Select(choices=AVAILABLE_MONTHS),
            'day': forms.Select(choices=AVAILABLE_DAYS),
            'time': forms.Select(choices=AVAILABLE_HOURS),
            'user': forms.HiddenInput(),
            'car': forms.HiddenInput(),
            'track': forms.HiddenInput(),
        }

    def __init__(self, user, car, track, *args, **kwargs):
        self.user = user
        self.car = car
        self.track = track
        super(BookingDateForm, self).__init__(*args, **kwargs)

    def save(self, commit=True):
        instance = super(BookingDateForm, self).save(commit=False)
        instance.user = self.user
        instance.car = self.car
        instance.track = self.track

        if commit:
            instance.save()

        return instance
