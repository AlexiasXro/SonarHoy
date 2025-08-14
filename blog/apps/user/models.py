from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(
        upload_to='avatars/',
        default='avatars/default-avatar.png',
        null=True,
        blank=True,
        max_length=200
    )

    def __str__(self):
        return f'Perfil de {self.user.username}'
    
@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    else:
        instance.profile.save()

        
    @property
    #Roles de usuario
    # Verifica si el usuario es un Miembros/Registrado
    def is_Members(self):
        return self.user.groups.filter(name='Miembros').exists() 
    
    @property
    # Verifica si el usuario es colaborador
    def is_collaborator(self):
        return self.user.groups.filter(name='Colaboradores').exists()
    
    @property
    def is_admin(self):
        return self.user.groups.filter(name='Administradores').exists()




