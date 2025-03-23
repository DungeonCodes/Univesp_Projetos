from django.db import models
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
    
