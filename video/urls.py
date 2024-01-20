from django.urls import path
from . import views

app_name = 'video'

urlpatterns = [
    path('', views.video_download_get_view, name='video_download_get'),
    path('watch/', views.video_watch_view, name='video_watch'),
    path('download/', views.video_download_view, name='video_download'),
    path('add_comment_api/', views.video_add_comment_api, name='add_comment'),
    path('test/', views.video_url_change_view, name='test'),
]