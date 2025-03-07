from django.db import models

class Prontuario(models.Model):
    codigo_barras = models.CharField(max_length=100, unique=True)
    nome_paciente = models.CharField(max_length=255)
    data_nascimento = models.DateField()
    ultima_consulta = models.DateTimeField(null=True, blank=True)

    # ADICIONE ESTE CAMPO PARA FORÇAR UMA MUDANÇA
    observacoes = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.nome_paciente
