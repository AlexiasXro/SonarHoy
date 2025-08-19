from django.apps import AppConfig


from django.apps import AppConfig

class UserConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.user'

    def ready(self):
        # Cargar signals automáticamente al iniciar la app
        import apps.user.signals
