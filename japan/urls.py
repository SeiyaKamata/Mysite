from django.urls import path
from . import views

app_name = 'japan'

urlpatterns = [
    path('', views.JapanView.as_view(), name='index'),
    path('list/', views.place_list_view, name='list'),
    path('add/', views.place_add_view, name='add'),
]