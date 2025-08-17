from django.contrib import admin
from .models import Evento
from django.utils.html import format_html

@admin.register(Evento)
class EventoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'fecha', 'localidad', 'imagen_preview')
    list_filter = ('fecha', 'localidad')
    search_fields = ('titulo', 'localidad')

    def imagen_preview(self, obj):
        if obj.imagen:
            return format_html('<img src="{}" style="width: 60px; height: auto;" />', obj.imagen.url)
        return "-"
    imagen_preview.short_description = "Imagen"
