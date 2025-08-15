from django.shortcuts import render, get_object_or_404
from .models import Evento
from collections import defaultdict
from datetime import date

def agenda(request):
    meses_es = [
        (1, "Enero"), (2, "Febrero"), (3, "Marzo"), (4, "Abril"),
        (5, "Mayo"), (6, "Junio"), (7, "Julio"), (8, "Agosto"),
        (9, "Septiembre"), (10, "Octubre"), (11, "Noviembre"), (12, "Diciembre")
    ]

    provincias_y_localidades = {
        "Ciudad Autónoma de Buenos Aires": [
            "Palermo", "Almagro", "Caballito", "San Telmo", "Flores", "Villa Crespo", 
            "Ciudad Universitaria", "Balvanera", "Chacarita", "Colegiales",
            "Núñez", "Retiro", "Microcentro", "Parque Patricios", "Liniers", 
            "Villa Soldati", "Villa Lugano",
        ],
        "Córdoba": ["Córdoba", "Cosquín", "Villa Carlos Paz"],
        "Buenos Aires": ["La Plata", "Mar del Plata", "Villa Gesell", "Zona Sur", "Zona Norte", "Zona Oeste"],
        "Santa Fe": ["Rosario", "Santa Fe"],  
        "Chaco": ["Resistencia"],
        "Río Negro": ["Bariloche"],
        "San Juan": ["San Juan"],
        "Mendoza": ["Mendoza"],
    }

    mes_seleccionado = request.GET.get('mes', '')
    localidad_seleccionada = request.GET.get('localidad', '')

    eventos_qs = Evento.objects.all().order_by('fecha')

    # Si no hay filtros → mostrar eventos desde hoy en adelante
    if not mes_seleccionado and not localidad_seleccionada:
        eventos_qs = eventos_qs.filter(fecha__gte=date.today())

    if mes_seleccionado:
        eventos_qs = eventos_qs.filter(fecha__month=mes_seleccionado)
    if localidad_seleccionada:
        eventos_qs = eventos_qs.filter(localidad=localidad_seleccionada)

    # Agrupar por fecha
    eventos_agrupados = defaultdict(list)
    for ev in eventos_qs:
        fecha_str = ev.fecha.strftime("%d/%m/%Y")
        eventos_agrupados[fecha_str].append(ev)

    localidades_disponibles = sorted(
        {loc for lista in provincias_y_localidades.values() for loc in lista}
    )

    return render(request, 'components/agenda.html', {
        'eventos': dict(eventos_agrupados),
        'meses_disponibles': meses_es,
        'localidades_disponibles': localidades_disponibles,
        'mes_seleccionado': mes_seleccionado,
        'localidad_seleccionada': localidad_seleccionada,
    })

def evento_agenda(request, evento_id):
    evento = get_object_or_404(Evento, id=evento_id)
    return render(request, 'components/evento_agenda.html', {'evento': evento})
