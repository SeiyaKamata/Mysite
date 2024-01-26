from django.db import transaction
from .models import Song, Artist, Genre

def add_song(name, genre, artist, url):
    try:
        with transaction.atomic():
            song = Song(
                name   = name,
                genre  = Genre.objects.get(id=genre),
                artist = Artist.objects.get(id=artist),
                url    = url,
            )
            song.save()

            return song
    except:
        return None


def add_artist(artist_name):
    try:
        with transaction.atomic():
            artist = Artist(
                name = artist_name,
            )
            artist.save()

            return artist
    except:
        return None