from django import forms
from .models import Contacto

class ContactoForm(forms.ModelForm):
    class Meta:
        model = Contacto
        fields = ['nombre_apellido', 'es_usuario', 'correo', 'tipo_consulta', 'mensaje']

        # clases reutilizables: claro (bg-white/text-gray-900) y oscuro (dark:bg-gray-800/dark:text-white)
        base_classes = (
            "w-full px-3 py-2 rounded border border-[#605dff] "
            "focus:outline-none focus:ring-2 focus:ring-[#605dff] "
            "bg-white text-gray-900 dark:bg-gray-800 dark:text-white"
        )

        widgets = {
            'nombre_apellido': forms.TextInput(attrs={
                'class': base_classes,
                'placeholder': 'Nombre y Apellido',
                'autocomplete': 'name',
            }),
            'es_usuario': forms.CheckboxInput(attrs={
                'class': (
                    "h-4 w-4 text-[#605dff] rounded border-gray-300 "
                    "focus:ring-[#605dff] dark:border-gray-600 dark:bg-gray-800"
                )
            }),
            'correo': forms.EmailInput(attrs={
                'class': base_classes,
                'placeholder': 'tu@correo.com',
                'autocomplete': 'email',
            }),
            'tipo_consulta': forms.Select(attrs={
                'class': base_classes + " pr-8",  # espacio para la flecha del select
            }),
            'mensaje': forms.Textarea(attrs={
                'class': base_classes,
                'rows': 6,
                'maxlength': 400,
                'placeholder': 'Escribe tu mensaje…',
            }),
        }
