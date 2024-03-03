from django.contrib.auth import authenticate
from django.contrib.auth.hashers import make_password
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from ..models import Usuario


class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['username', 'nome_completo', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data.get('password'))
        return super().create(validated_data)


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()

    def auth_usuario(self, data):
        email = data['email']
        password = data['password']
        usuario_existente = Usuario.objects.get(email=email)
        if usuario_existente is not None:
            username = usuario_existente.username
            user_para_login = authenticate(username=username, password=password)
            if user_para_login is not None:
                return user_para_login
        else:
            raise ValidationError("Usuário não cadastrado!")


class UsuarioPageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ('nome_completo', 'username')
