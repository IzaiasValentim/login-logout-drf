"""
URL configuration for api project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

# Roteador para rotas do ModelViewSet
from rest_framework.routers import SimpleRouter
from usuarios.api.views import UsuarioViewSet, UsuarioPageView, LoginUsuario, LogoutUsuario

# Views para o Swagger
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

router = SimpleRouter()
router.register('usuarios', UsuarioViewSet, basename='usuarios-views')

urlpatterns = [
                  path('admin/', admin.site.urls),

                  # Swagger:
                  path('schema/', SpectacularAPIView.as_view(), name='schema'),
                  path('swagger/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),

                  # Acesso do usuário:
                  path('login/', LoginUsuario.as_view(), name='login-usuário'),
                  path('logout/', LogoutUsuario.as_view(), name='login-usuário'),
                  path('user/', UsuarioPageView.as_view(), name='page-user'),
              ] + router.urls
