from django.urls import path
from . import views

app_name = 'anime'

urlpatterns = [
    path('', views.anime_list_view, name='list'),
    path('add/', views.anime_add_view, name='add'),
    path('detail/', views.anime_detail_view, name='detail'),
    path('add_comment_api/', views.anime_comment_add_api, name='add_comment'),
]