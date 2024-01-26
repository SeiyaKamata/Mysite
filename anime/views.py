from django.views.generic import TemplateView
from django.views import generic
from django.shortcuts import render, redirect
from django.http import JsonResponse

from .models import Anime, Genre, Period, Company
from .db import (
    add_anime,
    add_comment,
    get_anime_by_id, 
    get_animes_by_period_genre,
    get_places_by_anime,
    get_songs_by_anime,
    get_comments_by_anime,
)
from video.db import (
    get_videos_by_anime,
)


def custom_sort(period):
    year = period.year
    season = period.season
    season_order = {"冬": 1, "春": 2, "夏": 3, "秋": 4}
    return (year, season_order.get(season, 5))

def anime_comment_add_api(request):
    anime = request.POST.get('anime', 0)
    comment  = request.POST.get('comment', '')

    c = add_comment(anime, comment)

    return JsonResponse({'new_comment': c.comment})


def anime_list_view(request):
    genre = request.GET.getlist('g[]')
    period = request.GET.getlist('p[]')

    if not genre and not period:
        period = ['1',]

    if genre:
        genre = [int(g) for g in genre]

    if period:
        period = [int(p) for p in period]

    anime_list = get_animes_by_period_genre(period, genre)

    context = {
        'anime_list': anime_list,
        'genre': Genre.objects.all(),
        'period': sorted(Period.objects.all(), key=custom_sort),
        'selected_genre': genre,
        'selected_period': period,
    }

    return render(request, 'anime/anime_list.html', context)

def anime_detail_view(request):
    anime_id = request.GET.get('id', None)
    anime, genre, period = get_anime_by_id(anime_id)

    context = {
        'anime' :   anime,
        'genre' :   genre,
        'period':   period,
        'places':   get_places_by_anime(anime_id),
        'songs' :   get_songs_by_anime(anime_id),
        'videos':   get_videos_by_anime(anime_id),
        'comments': get_comments_by_anime(anime_id),
    }

    return render(request, 'anime/anime_detail.html', context)

def anime_add_view(request):
    if request.method == 'POST':
        name       = request.POST.get('name', '')
        genre      = request.POST.getlist('genre')
        period     = request.POST.getlist('period')
        image      = request.FILES.get('image')
        official   = request.POST.get('official_page', '')
        created_by = request.POST.get('created_by', '')

        anime = add_anime(name, genre, period, image, official, created_by)
        if anime is None:
            return redirect('/anime')
        return redirect('/anime')

    else:
        context = {
            'genre': Genre.objects.all(),
            'period': sorted(Period.objects.all(), key=custom_sort),
            'company': Company.objects.all(),
        }

    return render(request, 'anime/anime_add.html', context)