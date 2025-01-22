from modules.users.models import Users

class UsersService:
    @staticmethod
    def get_user_by_email(email: str) -> Users:
        return Users.objects.filter(email=email).first()

