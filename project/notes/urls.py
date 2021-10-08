from django.urls import path
from .views import NoteView
from .views import GreetingView
from .views import FilterView
from .views import SavingView
from .views import TemplateView
from .views import FindingView

urlpatterns = [
    path('notes/', NoteView.as_view(), name='notes'),
    path('greeting/', GreetingView.as_view(), name='greeting'),
    path('filter/', FilterView.as_view(), name='filter'),
    path('notes/save/', SavingView.as_view(), name='saving notes'),
    path('notes/find/', FindingView.as_view(), name='finding notes'),
    path('template/', TemplateView.as_view(), name='template')
]