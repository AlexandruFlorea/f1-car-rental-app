from django.shortcuts import render

def homepage_view(request):
    return render(request, 'homepage.html', {
        'title': 'Formula 1 experience',
        'favourites': [{
            'name': 'Mercedes AMG',
            'value': '367'
        }, {
            'name': 'Ferrari',
            'value': '333'
        }, {
            'name': 'McLaren',
            'value': '270'
        }, {
            'name': 'RedBull Racing',
            'value': '250'
        }]

    })