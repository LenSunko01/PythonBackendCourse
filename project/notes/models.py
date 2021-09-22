from django.db import models
from datetime import datetime


class Note(models.Model):
    RED = 'RE'
    BLUE = 'BL'
    YELLOW = 'YE'
    GREEN = 'GR'
    PURPLE = 'PU'
    RANDOM = 'RN'
    COLOR = [
        (RED, 'RE'),
        (BLUE, 'BL'),
        (YELLOW, 'YE'),
        (GREEN, 'GR'),
        (PURPLE, 'PU'),
        (RANDOM, 'RN')
    ]
    note_color = models.CharField(
        max_length=2,
        choices=COLOR,
        default=RANDOM,
    )
    note_text = models.CharField(max_length=200, default='SOME TEXT')
    note_name = models.CharField(max_length=20, default='SOME NAME')
    note_created = models.DateField(auto_now_add=True)
    note_first_word = models.CharField(max_length=15, default='FIRST')
    note_second_word = models.CharField(max_length=15, default='SECOND')
    note_third_word = models.CharField(max_length=15, default='THIRD')
    note_longest_word = models.CharField(max_length=15, default='LONGEST')
    note_shortest_word = models.CharField(max_length=15, default='SHORTEST')
