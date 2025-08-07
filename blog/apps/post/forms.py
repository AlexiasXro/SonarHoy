from django import forms

##### CLASE CON PABLO

# class PostFilterForm(forms.Form):
#     search_query = forms.CharField(
#         required=False,
#         widget=forms.TextInput(attrs={
#             'placeholder': 'Buscar posts...',
#             'class': 'form-control',}
#     )
#     )
#     order_by = forms.ChoiceField(
#         required=False,
#         choices=[
#             ('-created_at', 'Más recientes'),
#             ('created_at', 'Más antiguos'),
#             ('comments_count', 'Más comentados'),
#         ],
#     )    