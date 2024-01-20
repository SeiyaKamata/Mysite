from django.db import models


class Artist(models.Model):
    name = models.CharField('アーティスト名', max_length=200)

    def __str__(self):
        return self.name 

class Genre(models.Model):
    name = models.CharField('ジャンル名', max_length=200)

    def __str__(self):
        return self.name 


class Song(models.Model):
    name   = models.CharField('曲名', max_length=200)
    artist = models.ForeignKey(
                Artist,
                on_delete = models.PROTECT,
                verbose_name ="アーティスト"
             )
    url    = models.URLField('リンク', max_length=200)
    genre  = models.ForeignKey(
                Genre,
                on_delete = models.PROTECT,
                verbose_name ="ジャンル"
             )

    def __str__(self):
        return self.name