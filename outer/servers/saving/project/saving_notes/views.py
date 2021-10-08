from django.views import View
from rest_framework.parsers import JSONParser
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from .services import *
from django.http import JsonResponse
import json


@method_decorator(csrf_exempt, name='dispatch')
class NoteView(View):
    def patch(self, request):
        data = json.loads(request.body.decode("utf-8"))
        ok, result = update_note_name(data)
        if ok:
            return JsonResponse({ "message": "Successfully updated" }, status=200)
        else:
            return result

    def post(self, request):
        data = JSONParser().parse(request)
        ok, result = create_note(data)
        if ok:
            return JsonResponse(result.data, status=201)
        else:
            return result