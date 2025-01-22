from decouple import config

AUTH_USER_MODEL = "users.Users"

CSRF_TRUSTED_ORIGINS = config("CSRF_TRUSTED_ORIGINS").split(" ")
