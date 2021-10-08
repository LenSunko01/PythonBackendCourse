from django.urls import path
from .views import FindingView

urlpatterns = [
    path('notes/', FindingView.as_view(), name='notes'),
]