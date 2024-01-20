from django.shortcuts import render, redirect

from .models import Song, Genre, Artist
from anime.models import Anime
from .db import add_song
from anime.db import add_anime_song

def song_list_view(request):
    song = Song.objects.all()
    context = {
        'songs': song,
    }

    return render(request, 'song/song_list.html', context)

def song_add_view(request):
    if request.method == 'POST':
        name   = request.POST.get('name', '')
        genre  = request.POST.get('genre', 0)
        artist = request.POST.get('artist', 0)
        url    = request.POST.get('url', '')

        song = add_song(name, genre, artist, url)

        if genre == "1":
            anime = request.POST.get('anime', 0)
            add_anime_song(anime, song.id)

        if song is None:
            return redirect('/song')
        return redirect('/song')

    else:
        selected_anime = request.GET.get('anime_id', 0)

        context = {
            'genres':  Genre.objects.all(),
            'artists': Artist.objects.all(),
            'animes':  Anime.objects.all(),
            'selected_anime': int(selected_anime),
        }

    return render(request, 'song/song_add.html', context)