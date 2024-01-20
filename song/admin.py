from django.contrib import admin
from .models import Song, Artist, Genre

admin.site.register(Song)
admin.site.register(Genre)
admin.site.register(Artist)