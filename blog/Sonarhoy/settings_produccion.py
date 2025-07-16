from os import getenv

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = getenv('SECRET_KEY')
if SECRET_KEY is None:
    raise ValueError("The SECRET_KEY environment variable is not set.")

# TODO: Agrega aquí tus dominios permitidos
ALLOWED_HOSTS = [

]

# Database
# https://docs.djangoproject.com/en/5.2/ref/settings/#databases
# TODO: Configura tu base de datos aquí
DATABASES = {

}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.2/howto/static-files/

# TODO: URL para acceder a los archivos estáticos
STATIC_URL = 'static/'
# TODO: Define el directorio donde se recopilarán los archivos estáticos en producción
STATIC_ROOT = None
# TODO: Ruta donde se encuentran los archivos subidos por los usuarios
MEDIA_ROOT = None
# TODO: URL para acceder a los archivos subidos por los usuarios
MEDIA_URL = None