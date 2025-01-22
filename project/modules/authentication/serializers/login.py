from rest_framework import serializers
from modules.users.models import Users

class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = [
            'email',
            'password'
        ]

        