from django.contrib.auth import login, logout
from rest_framework import status
from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from .serilizers import UsuarioSerializer, LoginSerializer
from ..models import Usuario


class UsuarioViewSet(viewsets.ModelViewSet):
    serializer_class = UsuarioSerializer
    permission_classes = [AllowAny, ]
    queryset = Usuario.objects.all()

    http_method_names = ['get', 'post', ]


class LoginUsuario(APIView):
    permission_classes = [AllowAny, ]
    authentication_classes = [SessionAuthentication, ]

    def post(self, request):
        data = request.data
        serializer_login = LoginSerializer(data=data)
        if serializer_login.is_valid(raise_exception=True):
            usuario = serializer_login.auth_usuario(data=data)
            login(request, usuario)
            return Response({'Logado': usuario.username}, status=status.HTTP_200_OK)


class LogoutUsuario(APIView):
    permission_classes = [AllowAny, ]

    def post(self, request):
        usuario = request.user
        if usuario is not None:
            logout(request)
            return Response({'Usuario deslogado': usuario.username}, status=status.HTTP_200_OK)
        else:
            return Response({'Inválido': 'Não há uma sessão ativa'}, status=status.HTTP_200_OK)


