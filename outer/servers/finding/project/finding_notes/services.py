from .models import Note
import random
from .serializers import NoteSerializer
from .filtering_criterion import *
from django.http import JsonResponse


def filter(name_filter, color_filter):
    items = Note.objects.all()

    items_data = []
    for item in items:
        if name_filter is not None and item.note_name != name_filter:
            continue
        if color_filter is not None and item.note_color != color_filter:
            continue
        items_data.append(item)
    return NoteSerializer(items_data, many=True)