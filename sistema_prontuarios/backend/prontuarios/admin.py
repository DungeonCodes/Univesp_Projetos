from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Prontuarios, SisUser  # Importe o modelo
# modo de visualização no admin do Django prontuários
@admin.register(Prontuarios)
class ProntuarioAdmin(admin.ModelAdmin):
    list_display = ('micro_area','family','credential_id', 'name', 'last_name')
    search_fields = ('name', 'credential_id','family','micro_area')
    list_filter = ('family','micro_area')
# modo de visualização no admin do Django prontuários
@admin.register(SisUser)    
class SisUserAdmin(UserAdmin):
    list_display = ['username', 'email', 'first_name', 'last_name']
    search_fields = ('username', 'email')
    list_filter = ['user_level', 'is_staff', 'is_superuser']
