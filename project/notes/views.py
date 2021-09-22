from django.views import View
from rest_framework.parsers import JSONParser
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from .services import *
from django.http import JsonResponse


@method_decorator(csrf_exempt, name='dispatch')
class GreetingView(View):
    def get(self, request):
        return JsonResponse({"message": "Hi! This application is called Post-It Note. It should help you not to forget "
                                        "some important things"}, status=200)


@method_decorator(csrf_exempt, name='dispatch')
class NoteView(View):
    def get(self, request):
        name = request.GET.get("name")
        if name is None:
            notes_serializer = get_all_notes()
        else:
            notes_serializer = get_notes_with_given_name(name)
        return JsonResponse(notes_serializer.data, safe=False)

    def post(self, request):
        data = JSONParser().parse(request)
        ok, result = init_note(data)
        if ok:
            return JsonResponse(result.data, status=201)
        else:
            return result
