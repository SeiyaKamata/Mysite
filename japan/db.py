from django.db import transaction
from .models import Place

def add_place(name, address):
    try:
        with transaction.atomic():
            place = Place(
                name    = name,
                address = address,
            )
            place.save()

            return place
    except:
        return None