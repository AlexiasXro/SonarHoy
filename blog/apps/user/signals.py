from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType 
from apps.user.models import User
#aplicación Django que administra perfiles y permisos de usuario.
from django.db.models.signals import post_save 
# escucha la señal post_save del modelo Usuario para crear o actualizar perfiles de usuario y asignar permisos según los roles de usuario.
from django.dispatch import receiver
#from apps.blog.models import Post, Comment, Category  
# cuando estén listos

@receiver(post_save, sender=User)
def creatr_group_and_permissions(sender, instance, created, **kwargs):
    if created and instance.is_superuser:
        try:
            #TODO: Definir los permisos de POST y de COMMENTS

            # Crear grupos y asignar permisos
            # Miembros
            member_group, created = Group.objects.get_or_create(name='Miembros')
            member_group.permissions.set(
                Permission.objects.filter(
                    codename__in=[
                       # Permisos sobre comentarios
                       "add_comment", "view_comment"
                       # Permisos sobre publicaciones
                       "view_post"
                       # Permisos sobre suscripciones
                       'add_subscription', 'view_subscription'
                       # Permisos sobre categorías, si aplican
                       "view_category"
                       # Permisos sobre "me gusta" o valoraciones (modelo Like)
                       "add_like", "view_like"
                       # Ver contenido exclusivo
                       "view_exclusivecontent",
                    ]
                )
            )
            

              # Colaboradores 
            collaborator_group, _ = Group.objects.get_or_create(name='Colaboradores')
            collaborator_group.permissions.set(
                Permission.objects.filter(
                    codename__in=[
               # Comentarios
               'add_comment', 'view_comment', 'change_comment', 'delete_comment',

               # Posts (pueden crear y editar los suyos)
               'add_post', 'view_post', 'change_post',

               # Likes
               'add_like', 'view_like',

               # Ver categorías y contenido exclusivo
               'view_category', 'view_exclusivecontent',
                ]))
            
            #  GRUPO: Administradores 
            admin_group, _ = Group.objects.get_or_create(name='Administradores')
            admin_group.permissions.set(Permission.objects.all())  # acceso total

            # Agregar superuser al grupo Administradores
            instance.groups.add(admin_group)
            
            print("Grupos y permisos asignados correctamente.")
        except Exception as e:
            print(f'Error al crear grupos y permisos: {e}') 

       
        