from django import forms
from .models import Contacto

class ContactoForm(forms.ModelForm):
    class Meta:
        model = Contacto
        fields = ['nombre_apellido', 'es_usuario', 'correo', 'tipo_consulta', 'mensaje']
        base_classes = "w-full px-3 py-2 border rounded bg-white dark:bg-gray-800 text-gray-900 dark:text-white border-[#605dff] focus:outline-none focus:ring-2 focus:ring-[#605dff]"

        widgets = {
            'nombre_apellido': forms.TextInput(attrs={
                'class': 'w-full px-3 py-2 border border-[#605dff] rounded bg-gray-800 text-white placeholder-gray-400'
            }),
            'correo': forms.EmailInput(attrs={
                'class': 'w-full px-3 py-2 border border-[#605dff] rounded bg-gray-800 text-white placeholder-gray-400'
            }),
            'tipo_consulta': forms.Select(attrs={
                'class': 'w-full px-3 py-2 border border-[#605dff] rounded bg-gray-800 text-white'
            }),
            'mensaje': forms.Textarea(attrs={
                'rows': 5,
                'maxlength': 400,
                'class': 'w-full px-3 py-2 border border-[#605dff] rounded bg-gray-800 text-white placeholder-gray-400'
            }),
        }
