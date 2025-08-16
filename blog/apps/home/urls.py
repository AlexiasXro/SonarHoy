from django.urls import path
from .views import HomeView  # importar la clase

urlpatterns = [
    path('', HomeView.as_view(), name='home'),  # usar as_view() para la clase
]