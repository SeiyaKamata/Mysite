from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone
import uuid


class Place(models.Model):
    name = models.CharField('名前', max_length=200)
    address = models.CharField('住所', max_length=200)

    def __str__(self):
        return self.name 