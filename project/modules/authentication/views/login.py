from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from modules.users.services import UsersService
from django.contrib.auth.hashers import check_password
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import generics
from modules.authentication.serializers import LoginSerializer
import re

class LoginView(generics.GenericAPIView):
    permission_classes = [AllowAny]
    serializer_class = LoginSerializer
    
    def post(self, request):
        email = request.data.get('email')
        password = str(request.data.get('password'))
        
        try:
            if re.match(r'^\S+@\S+\.\S+$', email):
                user = UsersService.get_user_by_email(email=email)

            if not user or not user.is_active:
                return Response({"error": "Credenciais inválidas"}, status=401)
        except:
            return Response({"error": "Credenciais inválidas"}, status=401)
        
        if check_password(str(password), str(user.password)):
            return self.jwt_generate(user)
        else:
            return Response({"error": "Credenciais inválidas"}, status=401)
        
    @staticmethod
    def jwt_generate(user):
        jwt = RefreshToken.for_user(user)
        return Response({
            'refresh': str(jwt),
            'access': str(jwt.access_token),
        }, status=200)