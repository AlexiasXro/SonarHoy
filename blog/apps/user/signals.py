# apps/user/signals.py

from django.contrib.auth.models import Group
from apps.user.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

@receiver(post_save, sender=User)
def assign_member_group(sender, instance, created, **kwargs):
    """
    Asigna automáticamente al grupo 'Miembros' cada vez que se crea un nuevo usuario.
    """
    if created:
        # Obtener o crear el grupo 'Miembros'
        member_group, _ = Group.objects.get_or_create(name='Miembros')
        # Agregar el usuario al grupo
        instance.groups.add(member_group)
