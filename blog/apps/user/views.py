from django.views import generic
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import CustomUserCreationForm, ProfileAvatarForm
from django.contrib.auth import get_user_model
from django.shortcuts import redirect
from django.contrib.auth import logout


# autenticación de usuarios y la gestión de perfiles
class LoginView(auth_views.LoginView):
    template_name = 'user/formulario.html'
    extra_context = {
        'title': 'Iniciar sesión',
        'extra_links': [
            { 'name': 'Crear una cuenta', 'route': 'user:register' },
        ],
    }

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Variable para detectar sesión invitado
        context['is_guest'] = self.request.session.get('guest_user', False)
        return context

    def form_valid(self, form):
        # Al iniciar sesión normal, eliminar sesión invitado si existe
        if self.request.session.get('guest_user'):
            try:
                del self.request.session['guest_user']
                del self.request.session['guest_name']
                del self.request.session['guest_avatar_url']
            except KeyError:
                pass
        return super().form_valid(form)


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
    template_name = 'user/password_change_form.html'
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


# función para login como invitado (fuera de las clases)
def guest_login(request):
    # Guardar en sesión que es usuario invitado
    request.session['guest_user'] = True

    # Si hay usuario autenticado, cerrar sesión
    if request.user.is_authenticated:
        logout(request)

    # Asignar nombre y avatar por defecto en sesión si quieres
    request.session['guest_name'] = 'Invitado'
    request.session['guest_avatar_url'] = '/static/icons/user-profile.png'

    return redirect('home')


# función para cerrar sesión de invitado
def guest_logout(request):
    try:
        del request.session['guest_user']
        del request.session['guest_name']
        del request.session['guest_avatar_url']
    except KeyError:
        pass
    return redirect('user:login')


User = get_user_model()


# gestión de perfiles de usuario
class ProfileView(LoginRequiredMixin, generic.UpdateView):
    template_name = 'user/profile.html'
    model = User
    fields = ['first_name', 'last_name', 'email']
    success_url = reverse_lazy('user:profile')

    extra_context = {
        'title': 'Perfil de usuario',
        'extra_links': [
            { 'name': 'Cambiar contraseña', 'route': 'user:password_change' },
        ],
    }

    def get_object(self):
        return self.request.user 

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.method == 'POST':
            context['avatar_form'] = ProfileAvatarForm(self.request.POST, self.request.FILES, instance=self.request.user.profile)
        else:
            context['avatar_form'] = ProfileAvatarForm(instance=self.request.user.profile)
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        avatar_form = ProfileAvatarForm(request.POST, request.FILES, instance=request.user.profile)
        user_form = self.get_form()
        if user_form.is_valid() and avatar_form.is_valid():
            user_form.save()
            avatar_form.save()
            return self.form_valid(user_form)
        return self.form_invalid(user_form)

# apps/user/views.py
from django.shortcuts import render

def perfil(request):
    user = request.user
    grupos = user.groups.all()  # queryset de grupos
    return render(request, "user/perfil.html", {"user": user, "grupos": grupos})

def user_type(self):
    g = self.groups.first()
    return g.name if g else "Sin grupo"

User.add_to_class("user_type", user_type)