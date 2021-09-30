from django.urls import path
from .views import NoteView
from .views import GreetingView
from .views import FilterView

urlpatterns = [
    path('notes/', NoteView.as_view(), name='notes'),
    path('greeting/', GreetingView.as_view(), name='greeting'),
    path('filter/', FilterView.as_view(), name='filter'),
]