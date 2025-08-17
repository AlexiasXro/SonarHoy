from django.urls import path
from . import views

urlpatterns = [
    path('', views.quienes_somos, name='quienes_somos'),
]
