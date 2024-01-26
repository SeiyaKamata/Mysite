from django.db import models

class Genre(models.Model):
    name = models.CharField('ジャンル名', max_length=200)

    def __str__(self):
        return self.name 


class Company(models.Model):
    name = models.CharField('出版社', max_length=200)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name 


class Book(models.Model):
    name            = models.CharField('タイトル', max_length=200)
    genre           = models.ManyToManyField(Genre, verbose_name='ジャンル')
    book_image      = models.ImageField(upload_to='images/book', blank=True, null=True)
    published_date  = models.DateField(verbose_name='出版日')
    published_by    = models.ForeignKey(
                        Company,
                        on_delete = models.PROTECT,
                        verbose_name ="出版社"
                    )

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class Comment(models.Model):
    anime   = models.ForeignKey(
                Book,
                on_delete = models.PROTECT,
                verbose_name ="本"
            )
    comment = models.CharField('コメント', max_length=1000)
    data    = models.DateField(auto_now=True)
