from django.contrib import admin

from .models import (
    Book,
    Genre,
    Company,
    Comment,
)

admin.site.register(Book)
admin.site.register(Genre)
admin.site.register(Company)
admin.site.register(Comment)
