from os import getenv
import os
from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent.parent


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = getenv('SECRET_KEY')
if SECRET_KEY is None:
    raise ValueError("The SECRET_KEY environment variable is not set.")

# TODO: Agrega aquí tus dominios permitidos
ALLOWED_HOSTS = ['127.0.0.1', ' deidad2028.pythonanywhere.com']

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
    }
}

# os.environ['DJANGO_PORT'] = '8080'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.2/howto/static-files/

# TODO: URL para acceder a los archivos estáticos
# URL pública para acceder a archivos estáticos
STATIC_URL = '/static/'

# Carpeta donde se recopilarán todos los archivos estáticos para producción
STATIC_ROOT = BASE_DIR / 'staticfiles'

# Archivos de medios (subidos por usuarios)
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'