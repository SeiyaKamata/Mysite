from django.db import models
import os

from anime.models import Anime


def get_video_file_path(instance, filename):
    upload_to = f'videos/{instance.anime.id}/'

    ext = filename.split('.')[-1]
    filename = f'{instance.anime.id}_{instance.episode}.{ext}'

    return os.path.join(upload_to, filename)

class Video(models.Model):
    name       = models.CharField('動画名', max_length=200)
    video_file = models.FileField(upload_to=get_video_file_path)
    episode    = models.IntegerField('話')
    anime      = models.ForeignKey(
                        Anime,
                        on_delete = models.PROTECT,
                        verbose_name ="アニメ"
                    )

    class Meta:
        ordering = ["anime", "episode"]

    def __str__(self):
        return f'{self.anime.name}/{str(self.episode)}話'

class Comment(models.Model):
    video   = models.ForeignKey(
                Video,
                on_delete = models.PROTECT,
                verbose_name ="動画"
            )

    comment = models.CharField('コメント', max_length=1000)
    data    = models.DateField(auto_now=True)
