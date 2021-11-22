from django import forms
from bookings.models import Booking
from utils.constants.booking_date_select import AVAILABLE_HOURS, AVAILABLE_MONTHS, \
    AVAILABLE_YEARS, AVAILABLE_DAYS


class BookingForm(forms.ModelForm):
#     class Meta:
#         model = Booking
#         widgets = {
#             'user': forms.HiddenInput(),
#             'year': forms.Select(choices=AVAILABLE_YEARS),
#             'month': forms.Select(choices=AVAILABLE_MONTHS),
#             'day': forms.Select(choices=AVAILABLE_DAYS),
#             'time': forms.Select(choices=AVAILABLE_HOURS)
#
#         }
#         fields = ['car', 'track', 'year', 'month', 'day', 'time']
    pass


class BookingDateForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['user', 'car', 'track', 'date']
        widgets = {
            'user': forms.HiddenInput(),
            'car': forms.HiddenInput(),
            'track': forms.HiddenInput(),
            'date': forms.HiddenInput(),

        }

    def __init__(self, user, car, track, date, *args, **kwargs):
        self.user = user
        self.car = car
        self.track = track
        self.date = date
        super(BookingDateForm, self).__init__(*args, **kwargs)

    def clean_user(self):
        user = self.cleaned_data['user']
        return user

    def clean_car(self):
        return self.cleaned_data['car']

    def clean_track(self):
        return self.cleaned_data['track']

    def clean_date(self):
        return self.cleaned_data['date']

    def save(self, commit=True):
        instance = super(BookingDateForm, self).save(commit=False)
        instance.user = self.user
        instance.car = self.car
        instance.track = self.track
        instance.date = self.date

        if commit:
            instance.save()

        return instance
