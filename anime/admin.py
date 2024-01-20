from django.contrib import admin
from .models import (
    Anime,
    Genre,
    Period,
    Comment,
    Company,
    Anime_Song,
    Anime_Place,
)

admin.site.register(Anime)
admin.site.register(Genre)
admin.site.register(Period)
admin.site.register(Company)
admin.site.register(Comment)
admin.site.register(Anime_Song)
admin.site.register(Anime_Place)