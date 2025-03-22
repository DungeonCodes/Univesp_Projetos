from django.db import models

class Prontuarios(models.Model):
    credential_id = models.BigIntegerField(unique=True,verbose_name="CNS")
    name = models.CharField(max_length=255,verbose_name="Nome")
    last_name = models.CharField(max_length=50,verbose_name="Sobrenome")
    micro_area = models.IntegerField(verbose_name="Microárea")
    family = models.IntegerField(verbose_name="Família")


    # ADICIONE ESTE CAMPO PARA FORÇAR UMA MUDANÇA
    observacoes = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.name}{self.last_name} Prontuário: {self.family}-{self.micro_area}"
    
