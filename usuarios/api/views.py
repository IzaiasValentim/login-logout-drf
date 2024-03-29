from django.contrib.auth import login, logout
from drf_spectacular.utils import extend_schema
from rest_framework import status, renderers
from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .serilizers import UsuarioSerializer, LoginSerializer, UsuarioPageSerializer
from ..models import Usuario


class UsuarioViewSet(viewsets.ModelViewSet):
    serializer_class = UsuarioSerializer
    permission_classes = [AllowAny, ]
    queryset = Usuario.objects.all()

    http_method_names = ['get', 'post', ]
    renderer_classes = [renderers.TemplateHTMLRenderer]
    template_name = 'usuarios/cadastro.html'

    def list(self, request, **kwargs):
        return Response()


class LoginUsuario(APIView):
    permission_classes = [AllowAny, ]
    authentication_classes = [SessionAuthentication, ]
    serializer_class = LoginSerializer

    renderer_classes = [renderers.TemplateHTMLRenderer]
    template_name = 'usuarios/login.html'

    def get(self, request):
        return Response()

    @extend_schema(request=LoginSerializer)
    def post(self, request):
        data = request.data
        serializer_login = LoginSerializer(data=data)
        if serializer_login.is_valid(raise_exception=True):
            usuario = serializer_login.auth_usuario(data=data)
            login(request, usuario)
            return Response({'Logado': usuario.username}, status=status.HTTP_200_OK)


class LogoutUsuario(APIView):
    permission_classes = [IsAuthenticated, ]
    authentication_classes = [SessionAuthentication, ]

    renderer_classes = [renderers.TemplateHTMLRenderer]
    template_name = 'usuarios/logout.html'

    def get(self, request):
        return Response()

    def post(self, request):
        usuario = request.user
        if usuario is not None:
            logout(request)
            return Response({'Usuario deslogado': usuario.username}, status=status.HTTP_200_OK)
        else:
            return Response({'Inválido': 'Não há uma sessão ativa'}, status=status.HTTP_200_OK)


class UsuarioPageView(APIView):
    permission_classes = [IsAuthenticated, ]
    authentication_classes = [SessionAuthentication, ]
    serializer_class = UsuarioPageSerializer

    def get(self, request):
        serializer = UsuarioPageSerializer(request.user)
        return Response({"Área": "Acesso do usuário", "usuário": serializer.data}, status=status.HTTP_200_OK)
