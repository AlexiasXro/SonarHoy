from .settings import BASE_DIR
from pathlib import Path

# FIXME MODIFICACION MARTU PARA VER IMAGENS
import os


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-+)#(yq9=*$7y1n!)$f0)&8y15c(5o=_go+-g6xef$a2l&@f4!6'

ALLOWED_HOSTS = []

# Database
# https://docs.djangoproject.com/en/5.2/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.2/howto/static-files/
STATIC_URL = 'static/'

BASE_DIR = Path(__file__).resolve().parent.parent

## FIXME -- MODS MARTU PARA VER IMAGENES

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# MEDIA_ROOT = BASE_DIR / '.media'
# MEDIA_URL = 'media/'

