from django.shortcuts import render, redirect
from django.conf import settings
from django.http import JsonResponse

import asyncio
import time
from asgiref.sync import sync_to_async

from .youtube import download_anime
from anime.models import Anime
from .models import Video
from .db import add_comment


async def video_download_view(request):
    if request.method == 'POST':
        anime_id = request.POST.get('anime', None)

        for num in range(1, 100):
            video   = request.POST.get(f'video-{num}', None)
            episode = request.POST.get(f'video-{num}-episode', 0)
            if video is None:
                break
            async_download_anime = sync_to_async(download_anime, thread_sensitive=False)
            asyncio.create_task(async_download_anime(video, episode, anime_id))

        return redirect(f'/anime/detail?id={anime_id}')


def video_add_comment_api(request):
    video    = request.POST.get('video', 0)
    comment  = request.POST.get('comment', '')

    c = add_comment(video, comment)

    return JsonResponse({'new_comment': c.comment})


def video_download_get_view(request):
    if request.method == 'GET':
        anime_id = request.GET.get('anime_id', 0)

        videos = []
        context = {
            'animes':         Anime.objects.all(),
            'videos':         videos,
            'selected_anime': int(anime_id)
        }

    return render(request, 'video/download.html', context)

def video_watch_view(request):

    anime_id = request.GET.get('anime_id', 0)
    episode = int(request.GET.get('episode', 0))
    videos = Video.objects.filter(anime__id=anime_id)
    
    context = {
        'video_id': videos.get(episode=episode).id,
        'video':    videos.get(episode=episode).video_file.url,
        'previous': videos.get(episode=episode).video_file.url,
        'next':     videos.get(episode=episode).video_file.url,
    }

    return render(request, 'video/watch.html', context)

def video_url_change_view(request):

    videos = Video.objects.all()

    for video in videos:
        file_name = f'{video.anime}_{video.episode}.webm'
        video.video_file.name = f'videos/{video.anime.id}/{file_name}'
        video.save()

    return render(request, 'video/download.html', {})