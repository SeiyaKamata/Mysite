from django.urls import path
from . import views

app_name = 'song'

urlpatterns = [
    path('', views.song_list_view, name='song_list'),
    path('add', views.song_add_view, name='song_add'),
    path('add_artist', views.artist_add_view, name='song_add'),
]