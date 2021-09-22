from django.urls import path
from .views import NoteView
from .views import GreetingView

urlpatterns = [
    path('notes/', NoteView.as_view(), name='notes'),
    path('greeting/', GreetingView.as_view(), name='greeting'),
]