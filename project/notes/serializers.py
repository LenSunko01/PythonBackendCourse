from rest_framework import serializers

class NoteSerializer(serializers.Serializer):
    note_text = serializers.CharField(max_length=200)
    note_name = serializers.CharField(max_length=20)
    note_tag = serializers.FloatField(default=0.0)
