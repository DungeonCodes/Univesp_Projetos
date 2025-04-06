from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid  # Importa a biblioteca uuid

class Professional(models.Model):
    id_professional = models.UUIDField(
        primary_key=True,
        editable=False,
        default=uuid.uuid4,
        verbose_name="ID Profissional"  # Campo ID sem acento
    )
    credential_id = models.BigIntegerField(unique=True, verbose_name="Matricula")
    name_professional = models.CharField(max_length=255, verbose_name="Nome")
    last_name_professional = models.CharField(max_length=50, verbose_name="Sobrenome")
    job_title = models.CharField(max_length=50, verbose_name="Cargo")
    usage = models.CharField(max_length=50, verbose_name="Permissões")


    def __str__(self):
        return f"{self.name_professional} {self.last_name_professional}"  # Removido acento



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
    micro_area = models.IntegerField(verbose_name="Microarea")   
    family = models.IntegerField(verbose_name="Familia")        

    def __str__(self):
        return f"{self.name}{self.last_name} Prontuario: {self.family}-{self.micro_area}" 

# Cria a relacao de Usuarios do sistema, com criptografia hash para senha
class SisUser(AbstractUser):
    id_user = models.OneToOneField(
        Professional,
        to_field="credential_id",
        related_name="Matricula",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        verbose_name="ID Usuario"  
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
    
class Team(models.Model):

    micro_area = models.IntegerField(
        primary_key=True,
        verbose_name="Microarea"
    )

    class Team(models.TextChoices):
        ENFERMAGEM = 'enf'
        MEDICO = 'med'
        FONOAUDIOLOGIA = 'fono'
        PSICOLOGIA = 'psico'
        DENTISTA = 'dent'
        OUTROS = 'other'
    
    team = models.CharField(
        max_length=30,
        choices=Team.choices,
        verbose_name="Equipe"
    )

    id_team = models.IntegerField(unique=True, verbose_name="ID Team")

class Transfer(models.Model):
    id_transfer = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4, verbose_name="ID Transferencia")  # Campo ID sem acento
    id_sender = models.ForeignKey(Professional, to_field="credential_id", related_name="sender", verbose_name="ID Administrativo")
    id_receiver = models.ForeignKey(Professional, to_field="credential_id", related_name="receiver", verbose_name="ID Receptor")
    checkout = models.DateTimeField(
        verbose_name="Data de check-out",
        editable=False
    )
    checkin = models.DateTimeField(
        verbose_name="Data de check-in",
        editable=False
    )
    cns = models.ForeignKey(Prontuarios, verbose_name="CNS")

    def __str__(self):
        return f"Saída Prontuário: {Prontuarios.micro_area}.{Prontuarios.family}. - Entrgue por: {Professional.name_professional} - Returado por: {Professional.name_professional}"