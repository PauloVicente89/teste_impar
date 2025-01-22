INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # dependencies
    "rest_framework",
    "rest_framework_swagger",
    "drf_yasg",
    "rest_framework_simplejwt",
    "django_extensions",
    'graphene_django',

    # local modules
    'modules.photo',
    'modules.car',
    'modules.users',
    'modules.authentication',
]