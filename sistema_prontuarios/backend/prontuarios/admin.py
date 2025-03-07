from django.contrib import admin
from .models import Prontuario  # Importe o modelo

@admin.register(Prontuario)
class ProntuarioAdmin(admin.ModelAdmin):
    list_display = ('codigo_barras', 'nome_paciente', 'data_nascimento', 'ultima_consulta')
    search_fields = ('nome_paciente', 'codigo_barras')
    list_filter = ('data_nascimento',)
