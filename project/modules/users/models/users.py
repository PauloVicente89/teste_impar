import uuid
from django.contrib.auth.models import AbstractUser
from django.db import models

class Users(AbstractUser):

    class Role(models.TextChoices):
        ADMIN = "ADMIN", "Administrador"
        USER = "USER", "Usuário"

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=80)
    email = models.EmailField(unique=True, max_length=80)
    role = models.CharField(choices=Role.choices)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]
    
    class Meta:
        app_label = "users"
        db_table = "users.user"

