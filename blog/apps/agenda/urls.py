from django.urls import path
from . import views

urlpatterns = [
    path('agenda/', views.agenda, name='agenda'),
    path('evento/<int:evento_id>/', views.evento_agenda, name='evento_agenda'),
]
