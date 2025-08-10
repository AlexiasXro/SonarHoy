from django.shortcuts import render
from .models import Integrante

def quienes_somos(request):
    integrantes = Integrante.objects.all()
    return render(request, 'components/quienes_somos.html', {'integrantes': integrantes})
