from django import forms
from .models import Comment


##### CLASE CON PABLO

class PostFilterForm(forms.Form):
    search_query = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={
            'placeholder': 'Buscar posts...',
            'class': 'form-control',}
    )
    )
    order_by = forms.ChoiceField(
        required=False,
        choices=[
            ('-created_at', 'Más recientes'),
            ('created_at', 'Más antiguos'),
            ('comments_count', 'Más comentados'),
        ],
    )    

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={
                'rows': 3,
                'placeholder': 'Escribe tu comentario...',
                'class': 'w-full p-2 border rounded bg-white text-gray-900 dark:bg-gray-800 dark:text-white dark:placeholder-gray-400'
            })
        }

