from django.test import SimpleTestCase
from unittest.mock import patch
from notes.services import *
from notes.models import Note

first_note_name = "My first note"
second_note_name = "My second note"
third_note_name = "My third note"

class ServicesTest(SimpleTestCase):
    def test_getMostCommonWords_noRepetitions(self):
        text = "Cat Dog Parrot Squirrel"
        result = get_most_common_words(text)
        assert(len(result) == 3)
        assert("Cat" in result)
        assert("Dog" in result)
        assert("Parrot" in result)
        assert("Squirrel" not in result)

    def test_getMostCommonWords_withRepetitions(self):
        text = "Cat Dog Parrot Squirrel Cat Squirrel Squirrel Parrot"
        result = get_most_common_words(text)
        assert(len(result) == 3)
        assert("Cat" in result)
        assert("Parrot" in result)
        assert("Squirrel" in result)
        assert("Dog" not in result)

    def test_getMostCommonWords_differentCase(self):
        text = "Cat cat cAt"
        result = get_most_common_words(text)
        assert(len(result) == 3)
        assert("Cat" in result)
        assert("cat" in result)
        assert("cAt" in result)

    def test_getLongestWord(self):
        text="Long Longer Longest"
        assert(get_longest_word(text) == "Longest")

        text="abc xyz"
        assert(get_longest_word(text) == "abc" or get_longest_word(text) == "xyz")

        text="xyz abc"
        assert(get_longest_word(text) == "abc" or get_longest_word(text) == "xyz")

    def test_getShortestWord(self):
        text="Short Shorter Shortest"
        assert(get_shortest_word(text) == "Short")

        text="abc xyz"
        assert(get_shortest_word(text) == "abc" or get_shortest_word(text) == "xyz")

        text="xyz abc"
        assert(get_shortest_word(text) == "abc" or get_shortest_word(text) == "xyz")

    def test_processText_shortText_returnFalse(self):
        note_dict = {}
        note_dict['note_text'] = "short text"
        self.assertFalse(process_text(note_dict))

    def test_processText_lessThanThreeDifferentWords_returnFalse(self):
        note_dict = {}
        note_dict['note_text'] = "long long long text"
        self.assertFalse(process_text(note_dict))

    def test_initNote_shortText_returnFalse(self):
        data = {"note_color":"RN","note_text":"short text","note_name":"name_name"}
        ok, _ = init_note(data)
        self.assertFalse(ok)