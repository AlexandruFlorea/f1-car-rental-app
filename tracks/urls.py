from django.urls import path
from tracks.views import show_all_tracks, show_track_details


app_name = 'tracks'

urlpatterns = [
    path('', show_all_tracks, name='all'),
    path('<int:track_id>/', show_track_details, name='details'),  # 'details' is the name of the link, to be used in html

]