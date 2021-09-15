from django.db import models

class Note(models.Model):
    note_text = models.CharField(max_length=200, default='SOME TEXT')
    note_name = models.CharField(max_length=20, default='SOME NAME')
    note_tag = models.FloatField(default=0.0)
