from django import forms
from bookings.models import Booking


class BookingDateForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['user', 'car', 'track', 'date', 'cost']
        widgets = {
            'user': forms.HiddenInput(),
            'car': forms.HiddenInput(),
            'track': forms.HiddenInput(),
            'date': forms.HiddenInput(),
            'cost': forms.HiddenInput(),

        }

    def __init__(self, user, car, track, date, cost, *args, **kwargs):
        self.user = user
        self.car = car
        self.track = track
        self.date = date
        self.cost = cost
        super(BookingDateForm, self).__init__(*args, **kwargs)

    def clean_user(self):
        user = self.cleaned_data['user']
        print(f'cleaned data of {user}')
        return user

    def clean_car(self):
        return self.cleaned_data['car']

    def clean_track(self):
        return self.cleaned_data['track']

    def clean_date(self):
        return self.cleaned_data['date']

    def clean_cost(self):
        return self.cleaned_data['cost']

    def save(self, commit=True):
        instance = super(BookingDateForm, self).save(commit=False)
        instance.user = self.user
        instance.car = self.car
        instance.track = self.track
        instance.date = self.date
        instance.cost = self.cost

        if commit:
            instance.save()

        return instance
