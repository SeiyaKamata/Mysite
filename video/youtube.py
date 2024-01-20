import os

from yt_dlp import YoutubeDL
from apiclient.discovery import build

from django.conf import settings

from asgiref.sync import sync_to_async

from anime.models import Anime
from .db import add_video, add_async_video
from anime.db import get_async_anime_by_id

youtube = build('youtube', 'v3', developerKey=settings.YOUTUBE_API_KEY)

def get_playlists(channel_id):
    playlists = []
    request = youtube.playlists().list(part="snippet", channelId=channel_id)

    while request != None:
        response = request.execute()
        request = youtube.playlists().list_next(request, response)

        for item in response['items']:
            playlist_id = item['id']
            title = item['snippet']['title']
            thumbnail = item['snippet']['thumbnails']['default']['url']
            playlist_info = {'id': playlist_id, 'title': title, 'thumbnail': thumbnail}
            playlists.append(playlist_info)
 
    return playlists


def get_videos_from_channel(channel_id):
    videos = []
    request = youtube.search().list(part="snippet, status", channelId=channel_id, type="video")


    while request != None:
        response = request.execute()
        request = youtube.search().list_next(request, response)


        for item in response['items']:
            if item['status']['privacyStatus'] != "public":
                continue
            video_id = item['id']
            title = item['snippet']['title']
            thumbnail = item['snippet']['thumbnails']['default']['url']
            playlist_info = {'id': video_id, 'title': title, 'thumbnail': thumbnail}
            videos.append(playlist_info)


    return videos


def get_video_info_from_id(video_id):
    response = youtube.videos().list(part="snippet", id=video_id).execute()
    video_info = response["items"][0]["snippet"]

    return video_info


def get_videos_from_playlist(playlist_id):
    videos = []
    request = youtube.playlistItems().list(part="snippet, status", playlistId=playlist_id)

    while request != None:
        response = request.execute()
        request = youtube.playlistItems().list_next(request, response)

        for item in response['items']:
            if item['status']['privacyStatus'] != "public":
                continue
            video_id = item['snippet']['resourceId']['videoId']
            title = item['snippet']['title']
            thumbnail = item['snippet']['thumbnails']['default']['url']
            playlist_info = {'id': video_id, 'title': title, 'thumbnail': thumbnail}
            videos.append(playlist_info)

    return videos


def get_option(video_format, path):
    option = {}
    # option['outtmpl'] = dir_path + '%(title)s.%(ext)s'
    option['outtmpl'] = path

    if video_format == "mp4":
        option['format'] = 'bestvideo+bestaudio/best'
        option['postprocessors'] = [{
                'key': 'FFmpegVideoConvertor',
                'preferedformat': 'mp4',
            }]

    elif video_format == "mp3":
        option['format'] = 'bestaudio/best'
        option['postprocessors'] = [{
                'key': 'FFmpegExtractAudio', 
                'preferredcodec': 'mp3',
                'preferredquality': '192'
            }]

    elif  video_format == "webm":
        option['format'] = 'bestvideo+bestaudio/best'

    return option


def download(id, option):
    with YoutubeDL(option) as ydl:
        ydl.download(id)

def download_anime(video_id, episode, anime_id):
    file_format = "webm"
    upload_to = os.path.join(settings.MEDIA_ROOT, 'videos', str(anime_id))
    anime = Anime.objects.get(id=anime_id)
    file_name = f'{anime}_{episode}.{file_format}'
    path = os.path.join(upload_to, file_name)
    option = get_option(file_format, path)

    download(video_id, option)

    name = f'{anime}_{episode}話'
    add_video(name, path, episode, anime_id)
    print('ダウンロード完了')