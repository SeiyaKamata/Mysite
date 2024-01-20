from django.urls import path
from . import views

app_name = 'japan'

urlpatterns = [
    path('', views.JapanView.as_view(), name='index'),
    path('add', views.place_add_view, name='add'),
]