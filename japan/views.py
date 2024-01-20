from django.views.generic import TemplateView
from django.shortcuts import render, redirect

from anime.models import Anime

from .db import add_place
from anime.db import add_anime_place

class JapanView(TemplateView):
    template_name = "japan/japan2.html"


def place_add_view(request):
    if request.method == 'POST':
        name   = request.POST.get('name', '')
        address  = request.POST.get('address', 0)
        anime  = request.POST.get('anime', 0)

        place = add_place(name, address)

        add_anime_place(anime, place.id)

        if place is None:
            return redirect('/japan')
        return redirect('/japan')

    else:
        selected_anime = request.GET.get('anime_id', 0)

        context = {
            'animes':  Anime.objects.all(),
            'selected_anime': int(selected_anime),
        }

    return render(request, 'japan/place_add.html', context)