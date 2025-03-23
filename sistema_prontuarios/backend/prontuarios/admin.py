from django.contrib import admin
from prontuarios.models import Prontuarios  # Importe o modelo

@admin.register(Prontuarios)
class ProntuarioAdmin(admin.ModelAdmin):
    list_display = ('micro_area','family','credential_id', 'name', 'last_name')
    search_fields = ('name', 'credential_id','family','micro_area')
    list_filter = ('family','micro_area')
