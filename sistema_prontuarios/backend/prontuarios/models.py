from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid # importa a biblioteca uuid

class Prontuarios(models.Model):
    id_prontuario = models.UUIDField(primary_key=True,editable=False, default=uuid.uuid4, verbose_name="ID Prontuário") # cria um campo id_prontuario do tipo UUIDField
    credential_id = models.BigIntegerField(unique=True,verbose_name="CNS")
    name = models.CharField(max_length=255,verbose_name="Nome")
    last_name = models.CharField(max_length=50,verbose_name="Sobrenome")
    micro_area = models.IntegerField(verbose_name="Microárea")
    family = models.IntegerField(verbose_name="Família")


    def __str__(self):
        return f"{self.name}{self.last_name} Prontuário: {self.family}-{self.micro_area}"

# cria a relaçao de Usuários do sistema, com criptografia hash para senha
class SisUser(AbstractUser):
    id_user = models.OneToOneField(Prontuarios, on_delete=models.CASCADE, null=True, blank=True, verbose_name="ID Usuário") 
    class UserLevel(models.TextChoices):
        ADMIN_APP = 'admin_app', 'Administrador do Sistema'
        ADMIN_STAFF = 'admin_staff', 'Administrador Gerencial'
        ADMIN_SAME = 'admin_same', 'Administrador do Same'
        USER = 'user', 'Usuário Comum'

    user_level = models.CharField(max_length=50, choices=UserLevel.choices, null=True, default=UserLevel.USER, verbose_name="Nível de Acesso")
    
  
    def __str__(self):
        return f"{self.username} - {self.email} - {self.get_user_level_display()}"