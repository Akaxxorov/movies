from django.shortcuts import render
from .models import Movie, MovieGenre, \
    MovieStatusChoices, MovieTypeChoices, Genre


def home(request):
    banners = Movie.objects.filter(type=MovieTypeChoices.BANNER)[:3]
    regular = Movie.objects.filter(type=MovieTypeChoices.REGULAR)

    context = {
        'banners': banners,
        'regular': regular
    }
    print(f"{banners=}")

    return render(request, 'index.html', context=context)
