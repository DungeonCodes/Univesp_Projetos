from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid  # Importa a biblioteca uuid

class Prontuarios(models.Model):
    id_prontuario = models.UUIDField(
        primary_key=True,
        editable=False,
        default=uuid.uuid4,
        verbose_name="ID Prontuario"  # Campo ID sem acento
    )
    credential_id = models.BigIntegerField(unique=True, verbose_name="CNS")
    name = models.CharField(max_length=255, verbose_name="Nome")
    last_name = models.CharField(max_length=50, verbose_name="Sobrenome")
    micro_area = models.IntegerField(verbose_name="Microarea")  # Removido acento
    family = models.IntegerField(verbose_name="Familia")        # Removido acento

    def __str__(self):
        return f"{self.name}{self.last_name} Prontuario: {self.family}-{self.micro_area}"  # Removido acento

# Cria a relacao de Usuarios do sistema, com criptografia hash para senha
class SisUser(AbstractUser):
    id_user = models.OneToOneField(
        Prontuarios,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        verbose_name="ID Usuario"  # Removido acento
    )

    class UserLevel(models.TextChoices):
        ADMIN_APP = 'admin_app', 'Administrador do Sistema'
        ADMIN_STAFF = 'admin_staff', 'Administrador Gerencial'
        ADMIN_SAME = 'admin_same', 'Administrador do Same'
        USER = 'user', 'Usuario Comum'  # Removido acento

    user_level = models.CharField(
        max_length=50,
        choices=UserLevel.choices,
        null=True,
        default=UserLevel.USER,
        verbose_name="Nivel de Acesso"  # Removido acento
    )

    def __str__(self):
        return f"{self.username} - {self.email} - {self.get_user_level_display()}"
