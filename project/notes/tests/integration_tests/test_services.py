from django.test import TestCase
from unittest.mock import patch
from notes.services import *
from notes.models import Note

first_note_name = "My first note"
second_note_name = "My second note"
third_note_name = "My third note"

class ServicesTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.first_note = Note.objects.create(note_name=first_note_name)
        cls.second_note = Note.objects.create(note_name=second_note_name)
        cls.third_note = Note.objects.create(note_name=third_note_name)

    def test_getAllNotes(self):
        serializer = get_all_notes()
        data = serializer.data
        self.assertEqual(len(data), 3)
        for note in data:
            name = note.get('note_name')
            assert(name == first_note_name or name == second_note_name or name == third_note_name)

    def test_getNotesWithGivenName_namePresent(self):
        Note.objects.create(note_name="reminder")
        Note.objects.create(note_name="reminder")
        serializer = get_notes_with_given_name("reminder")
        data = serializer.data
        self.assertEqual(len(data), 2)
        for note in data:
            name = note.get('note_name')
            assert(name=="reminder")

    def test_getNotesWithGivenName_nameNotPresent(self):
        serializer = get_notes_with_given_name("non_existent_name")
        data = serializer.data
        self.assertEqual(len(data), 0)

    def test_processText_longText_returnTrue(self):
        note_dict = {}
        note_dict['note_text'] = "good good text very good text not bad at all so beautiful"
        self.assertTrue(process_text(note_dict))
        self.assertEqual(note_dict['note_first_word'], "good")
        self.assertEqual(note_dict['note_second_word'], "text")
        self.assertEqual(note_dict['note_third_word'], "very")
        self.assertEqual(note_dict['note_longest_word'], "beautiful")
        self.assertEqual(note_dict['note_shortest_word'], "at")

    def test_processName_manyWords(self):
        note_dict = {}
        note_dict['note_name'] = "my first note"
        process_name(note_dict)
        self.assertEqual(note_dict['note_name'], "MY_FIRST_NOTE")

    def test_processName_oneWord(self):
        note_dict = {}
        note_dict['note_name'] = "note"
        process_name(note_dict)
        self.assertEqual(note_dict['note_name'], "NOTE")

    def test_processColor(self):
        note_dict = {}
        note_dict['note_color'] = Note.RANDOM
        process_color(note_dict)
        self.assertNotEqual(note_dict['note_color'], Note.RANDOM)

    def test_initNote_longTextRandomColor_returnTrue(self):
        data = {"note_color":"RN","note_text":"long beautiful text","note_name":"my note"}
        ok, serializer = init_note(data)
        self.assertTrue(ok)
        note_dict = serializer.data
        self.assertNotEqual(note_dict['note_color'], Note.RANDOM)
        self.assertEqual(note_dict['note_name'], "MY_NOTE")
        self.assertEqual(note_dict['note_first_word'], "long")
        self.assertEqual(note_dict['note_second_word'], "beautiful")
        self.assertEqual(note_dict['note_third_word'], "text")
        self.assertEqual(note_dict['note_longest_word'], "beautiful")
        self.assertEqual(note_dict['note_shortest_word'], "long")

    def test_initNote_longTextGreenColor_returnTrue(self):
        data = {"note_color":"GR","note_text":"long beautiful text","note_name":"note"}
        ok, serializer = init_note(data)
        self.assertTrue(ok)
        note_dict = serializer.data
        self.assertEqual(note_dict['note_color'], Note.GREEN)
        self.assertEqual(note_dict['note_name'], "NOTE")
        self.assertEqual(note_dict['note_first_word'], "long")
        self.assertEqual(note_dict['note_second_word'], "beautiful")
        self.assertEqual(note_dict['note_third_word'], "text")
        self.assertEqual(note_dict['note_longest_word'], "beautiful")
        self.assertEqual(note_dict['note_shortest_word'], "long")
