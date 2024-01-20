from django.db import models
import uuid

from song.models import Song
from japan.models import Place

class Genre(models.Model):
    name = models.CharField('ジャンル名', max_length=200)

    def __str__(self):
        return self.name 


class Period(models.Model):
    year   = models.IntegerField('放送年')
    season = models.CharField('放送シーズン', max_length=1)

    class Meta:
        ordering = ["year"]

    def __str__(self):
        return str(self.year) + self.season

class Company(models.Model):
    name = models.CharField('会社名', max_length=200)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name 


class Anime(models.Model):
    name          = models.CharField('アニメ名', max_length=200)
    genre         = models.ManyToManyField(Genre, verbose_name='ジャンル')
    period        = models.ManyToManyField(Period, verbose_name='放送時期')
    image         = models.ImageField(upload_to='images', blank=True, null=True)
    official_page = models.URLField(blank=True)
    created_by    = models.ForeignKey(
                        Company,
                        on_delete = models.PROTECT,
                        verbose_name ="制作会社"
                    )

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name

class Comment(models.Model):
    anime   = models.ForeignKey(
                Anime,
                on_delete = models.PROTECT,
                verbose_name ="アニメ"
            )
    comment = models.CharField('コメント', max_length=1000)
    data    = models.DateField(auto_now=True)

class Anime_Song(models.Model):
    anime = models.ForeignKey(
                Anime,
                on_delete = models.PROTECT,
                verbose_name ="アニメ"
            )
    song  = models.ForeignKey(
                Song,
                verbose_name ="曲",
                on_delete = models.PROTECT,
            )

    def __str__(self):
        return self.anime.name + ' / ' + self.song.name

class Anime_Place(models.Model):
    anime = models.ForeignKey(
                Anime,
                on_delete = models.PROTECT,
                verbose_name ="アニメ"
            )
    place  = models.ForeignKey(
                Place,
                verbose_name ="聖地",
                on_delete = models.PROTECT,
            )

    def __str__(self):
        return self.anime.name + ' / ' + self.place.name