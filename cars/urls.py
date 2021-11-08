from django.urls import path
from cars.views import show_all_cars, show_car_details, add_car_to_cart

app_name = 'cars'

urlpatterns = [
    path('', show_all_cars, name='all'),
    path('<int:car_id>/', show_car_details, name='details'),
    path('<int:car_id>/add_to_cart/', add_car_to_cart, name='add_to_cart'),

]
