from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# Custom User Creation Form
# This form extends the default UserCreationForm to include additional fields like email.   

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True, label="Correo electrónico")
    # first_name = forms.CharField(required=True, label="Nombre")
    # last_name = forms.CharField(required=True, label="Apellido")

    class Meta:
        model = User
        fields = ('username', 
                  #'first_name', 
                  #'last_name', 
                  'email')
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        # user.first_name = self.cleaned_data['first_name']
        # user.last_name = self.cleaned_data['last_name']
        if commit:
            user.save()
        return user
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('Este email ya está registrado.')
        return email
