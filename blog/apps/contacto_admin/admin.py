from django.contrib import admin
from .models import Contacto

@admin.register(Contacto)
class ContactoAdmin(admin.ModelAdmin):
    list_display = ('nombre_apellido', 'correo', 'tipo_consulta', 'es_usuario', 'fecha_envio')
    list_filter = ('tipo_consulta', 'es_usuario', 'fecha_envio')
    search_fields = ('nombre_apellido', 'correo', 'mensaje')
