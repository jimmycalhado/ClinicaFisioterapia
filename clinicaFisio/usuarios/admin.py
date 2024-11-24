from django.contrib import admin
from .models import Paciente, Fisioterapeuta

@admin.register(Paciente)
class PacienteAdmin(admin.ModelAdmin):
    list_display = ('user', 'cpf', 'telefone')
    search_fields = ('user__username', 'cpf')
    list_filter = ('user__is_active',)
    ordering = ('user__username',)
    readonly_fields = ('user',)

    fields = ('user', 'cpf', 'telefone')


@admin.register(Fisioterapeuta)
class FisioterapeutaAdmin(admin.ModelAdmin):
    list_display = ('user', 'cpf', 'telefone', 'registro_profissional')
    search_fields = ('user__username', 'cpf', 'registro_profissional')
    list_filter = ('user__is_active',)
    ordering = ('user__username',)
    readonly_fields = ('user',)

    fields = ('user', 'cpf', 'telefone', 'registro_profissional')



