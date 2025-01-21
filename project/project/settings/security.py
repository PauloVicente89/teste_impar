from decouple import config

AUTH_USER_MODEL = "users.User"

CSRF_TRUSTED_ORIGINS = config("CSRF_TRUSTED_ORIGINS").split(" ")
