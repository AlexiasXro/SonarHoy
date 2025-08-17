from django.contrib import admin
from .models import Integrante

@admin.register(Integrante)
class IntegranteAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'rol')
