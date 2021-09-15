from django.views import View
from django.http import JsonResponse
from .models import Note
from rest_framework.parsers import JSONParser
from .serializers import NoteSerializer
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt


@method_decorator(csrf_exempt, name='dispatch')
class GreetingView(View):
    def get(self, request):
        return JsonResponse({"message": "Hola!"}, status=200)

@method_decorator(csrf_exempt, name='dispatch')
class NoteView(View):
    def get(self, request):
        name = request.GET.get("name")
        items = Note.objects.all()
        
        items_data = []
        for item in items:
            if item.note_name == name:
                items_data.append(item)

        serializer = NoteSerializer(items_data, many=True)
        return JsonResponse(serializer.data, safe=False)

    def post(self, request):
        data = JSONParser().parse(request)
        serializer = NoteSerializer(data=data)

        if not serializer.is_valid():
            return JsonResponse(serializer.errors, status=400)

        note_dict = serializer.validated_data
        if len(note_dict.get('note_text')) < 3 or len(note_dict.get('note_name')) < 3:
            # return 422 Unprocessable Entity
            return JsonResponse(
                {"error": "note_text and note_name should contain at least 3 characters"},
                status=422)
        new_name = note_dict.get('note_name') + "updated"
        new_text = note_dict.get('note_text') + "updated"
        new_tag = note_dict.get('note_tag') * 10 + 1000
        note_dict.update(note_name=new_name)
        note_dict.update(note_text=new_text)
        note_dict.update(note_tag=new_tag)

        note = Note.objects.create(**serializer.data)

        serializer = NoteSerializer(note)
        return JsonResponse(serializer.data, status=201)
