from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class Usuario(AbstractUser):
    """
          A classe Gestor(AbstractUser) substitui o usuário padrão do Django por motivo de melhor
          personalização.

          Um gestor será um administrador da plataforma, sendo habilitado a publicar notícias,
          fotos e controle da transparência dos investimentos.

      """
