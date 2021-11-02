from django.urls import path
from cars.views import show_all_cars, show_car_details

app_name = 'cars'

urlpatterns = [
    path('', show_all_cars, name='all'),
    path('<int:car_id>/', show_car_details, name='details'),

]
