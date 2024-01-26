from django.db import transaction
from asgiref.sync import sync_to_async
from song.models import Song
from .models import (
    Anime,
    Company,
    Anime_Song,
    Anime_Place,
    Place,
    Comment
)

@sync_to_async
def get_async_anime_by_id(data_id):
    try:
        anime = Anime.objects.get(id=data_id)
        genre = anime.genre.all()
        period = anime.period.all()

        anime.image = anime.image.url

        return anime

    except Anime.DoesNotExist:
        return None

def get_anime_by_id(data_id):
    try:
        anime = Anime.objects.get(id=data_id)
        genre = anime.genre.all()
        period = anime.period.all()

        anime.image = anime.image.url

        return anime, genre, period

    except Anime.DoesNotExist:
        return None

def add_anime(name, genre, period, image, official, created_by):
    try:
        with transaction.atomic():
            anime = Anime(
                name          = name,
                image         = image,
                official_page = official,
                created_by    = Company.objects.get(id=created_by),
            )
            anime.save()
            anime.genre.set(genre)
            anime.period.set(period)

            return anime
    except:
        return None

def add_anime_song(anime, song):
    try:
        with transaction.atomic():
            anison = Anime_Song(
                anime = Anime.objects.get(id=anime),
                song  = Song.objects.get(id=song),
            )
            anison.save()

            return anison
    except:
        return None

def add_anime_place(anime, place):
    try:
        with transaction.atomic():
            seichi = Anime_Place(
                anime = Anime.objects.get(id=anime),
                place = Place.objects.get(id=place),
            )
            seichi.save()

            return seichi
    except:
        return None

def add_comment(anime, comment):
    try:
        with transaction.atomic():
            c = Comment(
                anime = Anime.objects.get(id=anime),
                comment = comment,
            )
            c.save()

            return c
    except:
        return None


def get_anime_by_id(data_id):
    try:
        anime = Anime.objects.get(id=data_id)
        genre = anime.genre.all()
        period = anime.period.all()

        anime.image = anime.image.url

        return anime, genre, period

    except Anime.DoesNotExist:
        return None

def get_animes_by_period_genre(period, genre):
    filtered_animes = Anime.objects.all()

    if genre:
        filtered_animes = filtered_animes.filter(genre__id__in=genre)

    if period:
        filtered_animes = filtered_animes.filter(period__id__in=period)

    serialized_data = [{'id': anime.id, 'name': anime.name, 'image': anime.image.url} for anime in filtered_animes]

    return serialized_data

def get_places_by_anime(anime_id):
    try:
        place = Anime_Place.objects.filter(anime__id=anime_id)
        return place

    except Anime_Place.DoesNotExist:
        return None

def get_songs_by_anime(anime_id):
    try:
        song = Anime_Song.objects.filter(anime__id=anime_id)
        return song

    except Anime_Song.DoesNotExist:
        return None

def get_comments_by_anime(anime_id):
    try:
        comments = Comment.objects.filter(anime__id=anime_id)
        return comments

    except Comment.DoesNotExist:
        return None
