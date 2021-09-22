from .models import Note
import random
from .serializers import NoteSerializer
from django.http import JsonResponse
from collections import Counter


def get_all_notes():
    items = Note.objects.all()
    return NoteSerializer(items, many=True)


def get_notes_with_given_name(name):
    items = Note.objects.all()

    items_data = []
    for item in items:
        if item.note_name == name:
            items_data.append(item)
    return NoteSerializer(items_data, many=True)


def get_most_common_words(text):
    splitted = text.split()
    return [word for word, word_count in Counter(splitted).most_common(3)]


def get_longest_word(text):
    return max(text.split(), key=len)


def get_shortest_word(text):
    return min(text.split(), key=len)


def process_text(note_dict):
    text = note_dict.get('note_text')
    most_common_words = get_most_common_words(text)
    if len(most_common_words) < 3:
        return False

    note_dict.update(note_first_word=most_common_words[0])
    note_dict.update(note_second_word=most_common_words[1])
    note_dict.update(note_third_word=most_common_words[2])

    longest_word = get_longest_word(text)
    note_dict.update(note_longest_word=longest_word)

    shortest_word = get_shortest_word(text)
    note_dict.update(note_shortest_word=shortest_word)
    return True


def process_name(note_dict):
    new_name = note_dict.get('note_name').replace(" ", "_").upper()
    note_dict.update(note_name=new_name)


def process_color(note_dict):
    new_color = note_dict.get('note_color')
    while new_color == Note.RANDOM:
        new_color = random.choice(list(Note.COLOR))[1]
    note_dict.update(note_color=new_color)


def init_note(data):
    serializer = NoteSerializer(data=data)

    if not serializer.is_valid():
        return JsonResponse(serializer.errors, status=400)

    note_dict = serializer.validated_data

    if not process_text(note_dict):
        #return 422 Unprocessable Entity
        return (False, JsonResponse(
            {"error": "note_text should contain at least 3 different words"},
            status=422))

    process_name(note_dict)
    process_color(note_dict)

    note = Note.objects.create(**serializer.data)
    return True, NoteSerializer(note)
