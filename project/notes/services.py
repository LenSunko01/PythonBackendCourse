from .models import Note
import random
from .serializers import NoteSerializer
from .paths import *
from .templates import *
from django.http import JsonResponse
from collections import Counter
import grpc
import requests
from protos import counter_pb2
from protos import counter_pb2_grpc


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


def get_notes_with_given_word(word):
    items = Note.objects.all()

    channel = grpc.insecure_channel('localhost:50051')
    stub = counter_pb2_grpc.CounterStub(channel)
    items_data = []
    for item in items:
        reply = stub.Count(counter_pb2.Text(text = item.note_text, word=word))
        if reply.number > 0:
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


def save_note(request):
    response = requests.post(SAVING_SERVICE_PATH, data = request.body)
    return JsonResponse(response.json(), status=response.status_code)


def update_note_name(request):
    response = requests.patch(SAVING_SERVICE_PATH, data = request.body)
    return JsonResponse(response.json(), status=response.status_code)


def get_template(type):
    if type is None:
        return JsonResponse({"error": "template name is not specified"}, status=400)
    if type not in TEMPLATE:
        return JsonResponse({"error": "template not found: " + type}, status=404)
    response = requests.get(TEMPLATE_SERVICE_PATH + type)
    return JsonResponse(response.json(), status=response.status_code)


def find_note(name_criterion, color_criterion):
    payload = {'name': name_criterion, 'color': color_criterion}
    response = requests.get(FINDING_SERVICE_PATH, params=payload)
    return JsonResponse(response.json(), status=response.status_code, safe=False)