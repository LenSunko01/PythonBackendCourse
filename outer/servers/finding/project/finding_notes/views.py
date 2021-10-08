from django.views import View
from rest_framework.parsers import JSONParser
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from .services import *
from django.http import JsonResponse


@method_decorator(csrf_exempt, name='dispatch')
class FindingView(View):
    def get(self, request):
        name_filter = request.GET.get("name")
        color_filter = request.GET.get("color")
        notes_serializer = filter(name_filter, color_filter)
        return JsonResponse(notes_serializer.data, safe=False)