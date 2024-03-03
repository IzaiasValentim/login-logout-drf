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
    nome_completo = models.CharField(max_length=100, null=False, blank=False)
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_atualizacao = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Usuarios'

    def __str__(self):
        return f'{self.username} - {self.email}'
