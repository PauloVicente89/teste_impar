from decouple import config
from datetime import timedelta

SECRET_KEY = config("SECRET_KEY")

SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(hours=72),  # Duração para o token de acesso
    "ROTATE_REFRESH_TOKENS": False,  # Rotacionar o refresh token
    "SIGNING_KEY": config("SECRET_KEY"),
    "ALGORITHM": "HS256",
    "AUTH_HEADER_TYPES": ("Bearer",),
    "AUTH_HEADER_NAME": "HTTP_AUTHORIZATION",
}

REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework_simplejwt.authentication.JWTAuthentication",
        "rest_framework.authentication.SessionAuthentication",
    ),
    "DEFAULT_PERMISSION_CLASSES": ("rest_framework.permissions.IsAuthenticated",),
}
