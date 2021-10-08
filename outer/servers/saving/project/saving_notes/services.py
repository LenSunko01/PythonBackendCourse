from .models import Note
import random
from .serializers import NoteSerializer
from django.http import JsonResponse
from collections import Counter
import grpc
from django.db.models import F

def create_note(data):
    serializer = NoteSerializer(data=data)

    if not serializer.is_valid():
        return False, JsonResponse(serializer.errors, status=400)

    note = Note.objects.create(**serializer.data)
    return True, NoteSerializer(note)

def update_note_name(dict):
    if "old_name" not in dict or "new_name" not in dict:
        return False, JsonResponse("Request body misses fields", status=400)
    old_name = dict['old_name']
    new_name = dict['new_name']
    notes = Note.objects.filter(note_name=old_name)
    for note in notes:
        note.note_name = new_name
        note.save()
    return True, None