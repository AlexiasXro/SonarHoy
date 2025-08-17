from os import getenv
import os

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = getenv('SECRET_KEY')
if SECRET_KEY is None:
    raise ValueError("The SECRET_KEY environment variable is not set.")

# TODO: Agrega aquí tus dominios permitidos
ALLOWED_HOSTS = ['127.0.0.1', 'midominio-production.com']

# Database
# https://docs.djangoproject.com/en/5.2/ref/settings/#databases
# TODO: Configura tu base de datos aquí

DATABASES = {
    'default': {
        #'ENGINE': 'django.db.backends.sqlite3',
        #'NAME': BASE_DIR / 'db.sqlite3',

        # En caso de usar una postgres
        # 'ENGINE': 'django.db.backends.postgresql',

       # En caso de usar una mysql

        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.getenv('DB_NAME'),
        'USER': os.getenv('DB_USER'),
        'PASSWORD': os.getenv('DB_PASSWORD'),
        'HOST': os.getenv('DB_HOST'),
        'PORT': os.getenv('DB_PORT'),
    }
}

os.environ['DJANGO_PORT'] = '8080'

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