from django.views import generic
from django.contrib.auth import views as auth_views, forms as auth_forms
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import CustomUserCreationForm
from django.contrib.auth import get_user_model




# autenticación de usuarios y la gestión de perfiles
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

# registro de usuario
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

# confirmar el registro de usuario exitoso
class UserCreateDoneView(generic.TemplateView):
    template_name = 'estado.html'
    extra_context = {
        'title': 'Cuenta creada',
        'message': 'Tu cuenta ha sido creada exitosamente. Ahora puedes iniciar sesión.',
    }



# gestión de contraseñas
class PasswordChangeView(auth_views.PasswordChangeView):
    template_name = 'user/formulario.html'
    extra_context = {
        'title': 'Cambiar contraseña',
    }
    success_url = reverse_lazy('user:password_change_done')


# confirmar el cambio de contraseña exitoso
class PasswordChangeDoneView(auth_views.PasswordChangeDoneView):
    template_name = 'estado.html'
    extra_context = {
        'title': 'Contraseña cambiada',
        'message': 'Tu contraseña ha sido cambiada exitosamente.',
    }



User = get_user_model()

# gestión de perfiles de usuario
# MODAL vista para editar el perfil del usuario
class ProfileView(LoginRequiredMixin, generic.UpdateView):
    template_name = 'user/profile.html'
    model = User
    fields = ['first_name', 'last_name', 'email']
    success_url = reverse_lazy('user:profile')

    extra_context = {
        'title': 'Perfil de usuario',
        'extra_links': [
            { 'name': 'Cambiar contraseña', 'route': 'user:password_change' },
            # { 'name': 'Ver publicaciones', 'route': 'blog:post_list' },
            
        ],
    
    }
    def get_object(self):
        return self.request.user 


#  vista para editar el avatar del perfil del usuario
def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.method == 'POST':
            context['avatar_form'] = ProfileAvatarForm(self.request.POST, self.request.FILES, instance=self.request.user.profile)
        else:
            context['avatar_form'] = ProfileAvatarForm(instance=self.request.user.profile)
        return context


