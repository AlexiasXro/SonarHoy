from django.views import generic
from django.contrib.auth import views as auth_views, forms as auth_forms
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import CustomUserCreationForm

class LoginView(auth_views.LoginView):
    template_name = 'user/formulario.html'
    extra_context = {
        'title': 'Iniciar sesión',
        'extra_links': [
            { 'name': 'Crear una cuenta', 'route': 'user:register' },
        ],
    }

class LogoutView(auth_views.LogoutView):
    next_page = 'user:login'

class UserCreateView(generic.CreateView):
    form_class = CustomUserCreationForm
    template_name = 'user/formulario.html'
    extra_context = {
        'title': 'Registrarse',
        'extra_links': [
            { 'name': 'Ir a Iniciar Sesión', 'route': 'user:login' },
        ],
    }
    success_url = reverse_lazy('user:login')

class ProfileView(LoginRequiredMixin, generic.TemplateView):
    template_name = 'user/profile.html'

class PasswordChangeView(auth_views.PasswordChangeView):
    template_name = 'user/formulario.html'
    extra_context = {
        'title': 'Cambiar contraseña',
    }
    success_url = reverse_lazy('user:password_change_done')

class PasswordChangeDoneView(auth_views.PasswordChangeDoneView):
    template_name = 'user/estado.html'
    extra_context = {
        'title': 'Contraseña cambiada',
        'message': 'Tu contraseña ha sido cambiada exitosamente.',
    }
