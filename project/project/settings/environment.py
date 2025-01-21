import os
from pathlib import Path
from decouple import config
import os
from .templates import BASE_DIR

BASE_DIR = Path(__file__).resolve().parent.parent.parent

DATA_DIR = BASE_DIR.parent / 'data' / 'web'

DEBUG = False

DEBUG = config("DEBUG", default=False, cast=bool)

ALLOWED_HOSTS = config("ALLOWED_HOSTS").split(" ")

STATIC_URL = "/static/"
STATIC_ROOT = "/data/web/static"
STATICFILES_DIRS = [BASE_DIR / 'static']

MEDIA_URL = "/media/"
MEDIA_ROOT = "/data/web/media"

ROOT_URLCONF = 'project.urls'

WSGI_APPLICATION = 'project.wsgi.application'

DJANGO_ADMIN_URL = config("DJANGO_ADMIN_URL", default="admin/")

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
