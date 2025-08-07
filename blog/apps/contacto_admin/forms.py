from django import forms
from .models import Contacto

class ContactoForm(forms.ModelForm):
    class Meta:
        model = Contacto
        fields = ['nombre_apellido', 'es_usuario', 'correo', 'tipo_consulta', 'mensaje']
        widgets = {
            'nombre_apellido': forms.TextInput(attrs={'class': 'w-full px-3 py-2 border border-[#605dff] rounded'}),
            'correo': forms.EmailInput(attrs={'class': 'w-full px-3 py-2 border border-[#605dff] rounded'}),
            'tipo_consulta': forms.Select(attrs={'class': 'w-full px-3 py-2 border border-[#605dff] rounded'}),
            'mensaje': forms.Textarea(attrs={'rows': 5, 'maxlength': 400, 'class': 'w-full px-3 py-2 border border-[#605dff] rounded'}),
        }
