from django.contrib import admin
from .models import Agendamento

@admin.register(Agendamento)
class AgendamentoAdmin(admin.ModelAdmin):
    list_display = ['paciente', 'data', 'horario', 'descricao']
    list_filter = ['data']
    search_fields = ['paciente__username', 'descricao']