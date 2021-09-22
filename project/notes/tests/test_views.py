from django.urls import reverse
from django.test import TestCase
from notes.models import Note
import json
from notes.serializers import NoteSerializer
from rest_framework.parsers import JSONParser

class ViewsTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.first_note = Note.objects.create(note_name="Reminder")
        cls.second_note = Note.objects.create(note_name="Notification")
        cls.third_note = Note.objects.create(note_name="Reminder")

    def test_greeting(self):
        response = self.client.get(reverse('greeting'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Hi! This application is called Post-It Note. It should help you not to forget "
                                        "some important things")

    def test_getNotes_withUrlParameter(self):
        response = self.client.get(reverse('notes'), {'name': 'Reminder'})
        self.assertEqual(response.status_code, 200)
        in_json = json.loads(response.content)
        serializer = NoteSerializer(data=in_json, many=True)
        assert(serializer.is_valid())
        note_dict = serializer.validated_data
        self.assertEqual(len(note_dict), 2)
        for note in note_dict:
            self.assertEqual(note['note_name'], "Reminder")

    def test_getNotes_noUrlParameter(self):
        response = self.client.get(reverse('notes'))
        self.assertEqual(response.status_code, 200)
        in_json = json.loads(response.content)
        serializer = NoteSerializer(data=in_json, many=True)
        assert(serializer.is_valid())
        note_dict = serializer.validated_data
        self.assertEqual(len(note_dict), 3)

    def test_postNote(self):
        note = Note(note_color=Note.RANDOM, note_text="text with words and words and words",
                    note_name="my note", note_created="2021-09-10")
        serializer = NoteSerializer(note)
        response = self.client.post(reverse('notes'), {'note_color': 'RN',
        'note_text': 'text with words and words and words', 'note_name': 'my note', 'note_created': '2021-09-22'},
        content_type='application/json')
        self.assertEqual(response.status_code, 201)
        in_json = json.loads(response.content)
        serializer = NoteSerializer(data=in_json)
        assert(serializer.is_valid())
        note_dict = serializer.validated_data
        self.assertNotEqual(note_dict['note_color'], Note.RANDOM)
        self.assertEqual(note_dict['note_name'], "MY_NOTE")
        self.assertEqual(note_dict['note_first_word'], "words")
        self.assertEqual(note_dict['note_second_word'], "and")
        self.assertEqual(note_dict['note_third_word'], "text")
        self.assertEqual(note_dict['note_longest_word'], "words")
        self.assertEqual(note_dict['note_shortest_word'], "and")