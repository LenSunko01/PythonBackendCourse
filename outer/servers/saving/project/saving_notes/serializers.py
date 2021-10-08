from rest_framework import serializers
from .models import Note
from rest_framework.fields import ChoiceField


class NoteSerializer(serializers.Serializer):
    note_color = ChoiceField(choices=Note.COLOR)
    note_text = serializers.CharField(max_length=200)
    note_name = serializers.CharField(max_length=20)
    note_created = serializers.DateField(required=False)
    note_first_word = serializers.CharField(max_length=15, required=False)
    note_second_word = serializers.CharField(max_length=15, required=False)
    note_third_word = serializers.CharField(max_length=15, required=False)
    note_longest_word = serializers.CharField(max_length=15, required=False)
    note_shortest_word = serializers.CharField(max_length=15, required=False)