from django.db import transaction
from asgiref.sync import sync_to_async

from .models import Video, Comment
from anime.models import Anime

def add_video(name, video_file, episode, anime_id):
    try:
        with transaction.atomic():
            video = Video(
                name       = name,
                video_file = video_file,
                episode    = episode,
                anime      = Anime.objects.get(id=anime_id),
            )
            video.save()

            return video
    except:
        return None

def add_comment(video, comment):
    try:
        with transaction.atomic():
            c = Comment(
                video   = Video.objects.get(id=video),
                comment = comment,
            )
            c.save()

            return c
    except:
        return None


@sync_to_async
def add_async_video(name, video_file, episode, anime_id):
    try:
        with transaction.atomic():
            video = Video(
                name       = name,
                video_file = video_file,
                episode    = episode,
                anime      = Anime.objects.get(id=anime_id),
            )
            video.save()

            return video
    except:
        return None


def get_videos_by_anime(anime_id):
    try:
        videos = Video.objects.filter(anime__id=anime_id)
        return videos

    except Video.DoesNotExist:
        return None