from django.contrib.auth import authenticate
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from ..models import Usuario


class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['username', 'nome_completo', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField
    password = serializers.CharField

    def auth_usuario(self, data):
        email_auth = data['email']
        password_auth = data['password']
        usuario_existente = Usuario.objects.get(email=email_auth)

        if usuario_existente is not None:
            user_para_login = authenticate(username=usuario_existente.username, password=password_auth)
            if user_para_login is not None:
                return user_para_login
        else:
            return ValidationError("Usuário não cadastrado!")
