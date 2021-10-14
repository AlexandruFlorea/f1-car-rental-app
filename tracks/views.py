from django.shortcuts import render

def track_selection(request):
    return render(request, 'tracks.html', {})