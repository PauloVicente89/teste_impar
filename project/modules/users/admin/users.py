from django.contrib import admin
from django.contrib.auth import admin as auth_admin
from modules.users.models import Users

@admin.register(Users)
class UsersAdmin(auth_admin.UserAdmin):
    list_display = [
        "email",
        "name",
        "is_active",
        "role",
    ]
    f = list(auth_admin.UserAdmin.fieldsets)
    f[1] = (
        "Informações Pessoais",
        {
            "fields": (
                "first_name",
                "email",
            )
        },
    )