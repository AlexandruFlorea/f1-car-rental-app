from django.urls import path
from tracks.views import track_selection


app_name = 'tracks'

urlpatterns = [
    path('tracks/', track_selection, name='tracks')
]