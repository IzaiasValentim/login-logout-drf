from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from .serilizers import UsuarioSerializer
from ..models import Usuario


class UsuarioViewSet(viewsets.ModelViewSet):
    serializer_class = UsuarioSerializer
    permission_classes = [AllowAny, ]
    queryset = Usuario.objects.all()

    http_method_names = ['get', 'post', ]



