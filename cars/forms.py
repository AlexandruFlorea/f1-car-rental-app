from django import forms
from cars.models import Category, Car
from bookings.models import Booking


ORDER_BY_CHOICES = (('POPULARITY', 'Popularity'), ('PRICE_ASC', 'Price ascending'), ('PRICE_DESC', 'Price descending'))


def get_orderby_field(order_by):
    if order_by == 'PRICE_ASC':
        return 'rate'

    if order_by == 'PRICE_DESC':
        return '-rate'

    if order_by == 'POPULARITY':

        return 'id'

    return 'id'


class FilterCarsForm(forms.Form):
    order_by = forms.ChoiceField(choices=ORDER_BY_CHOICES, required=False)
    powered_by = forms.MultipleChoiceField(choices=(), widget=forms.CheckboxSelectMultiple, required=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        categories = Category.objects.all()
        self.fields['powered_by'].choices = tuple((category.id, category.name) for category in categories)

    def clean_categories(self):
        categories = self.cleaned_data.get('powered_by', [])
        return categories

    def apply_filters(self):
        is_valid = self.is_valid()
        if is_valid:
            order_by = get_orderby_field(self.cleaned_data.get('order_by'))
            categories = self.cleaned_data.get('powered_by', [])

            cars = Car.objects.order_by(order_by)

            if len(categories) > 0:
                cars = cars.filter(category__id__in=categories)

            return cars

        return Car.objects.all()
