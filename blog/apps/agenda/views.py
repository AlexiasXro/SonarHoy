from django.shortcuts import render
from .models import Evento
from collections import defaultdict
import calendar

def agenda(request):
    # Filtros seleccionados por GET
    mes_seleccionado = request.GET.get('mes', '')
    anio_seleccionado = request.GET.get('anio', '')
    localidad_seleccionada = request.GET.get('localidad', '')

    # Query base
    eventos = Evento.objects.all()

    if mes_seleccionado:
        eventos = eventos.filter(fecha__month=mes_seleccionado)
    if anio_seleccionado:
        eventos = eventos.filter(fecha__year=anio_seleccionado)
    if localidad_seleccionada:
        eventos = eventos.filter(localidad=localidad_seleccionada)

    # Ordenar por fecha
    eventos = eventos.order_by('fecha')

    # Agrupar por fecha legible
    eventos_agrupados = defaultdict(list)
    for ev in eventos:
        fecha_str = ev.fecha.strftime("%d/%m/%Y")
        eventos_agrupados[fecha_str].append(ev)

    # Datos para los filtros
    meses_disponibles = [(i, calendar.month_name[i]) for i in range(1, 13)]
    anios_disponibles = sorted(set(e.fecha.year for e in Evento.objects.all()), reverse=True)
    localidades_disponibles = sorted(set(e.localidad for e in Evento.objects.all()))

    return render(request, 'components/agenda.html', {
        'eventos': dict(eventos_agrupados),
        'meses_disponibles': meses_disponibles,
        'anios_disponibles': anios_disponibles,
        'localidades_disponibles': localidades_disponibles,
        'mes_seleccionado': mes_seleccionado,
        'anio_seleccionado': anio_seleccionado,
        'localidad_seleccionada': localidad_seleccionada,
    })
