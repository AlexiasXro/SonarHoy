from django.urls import path
from .views import agenda

urlpatterns = [
    path('agenda/', agenda, name='agenda'),
]
