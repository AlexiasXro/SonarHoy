from django.urls import path
from . import views

app_name = 'user'

urlpatterns = [
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    
    path('register/', views.UserCreateView.as_view(), name='register'),
    path('password_change/', views.PasswordChangeView.as_view(), name='password_change'),
    path('password_change/done/', views.PasswordChangeDoneView.as_view(), name='password_change_done'),
    path('profile/', views.ProfileView.as_view(), name='profile'),
    path('guest-login/', views.guest_login, name='guest_login'),
    path('guest-logout/', views.guest_logout, name='guest_logout'),
    
]