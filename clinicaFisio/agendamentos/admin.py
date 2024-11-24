from django.contrib import admin
from .models import Agendamento, Disponibilidade, Fisioterapeuta

@admin.register(Agendamento)
class AgendamentoAdmin(admin.ModelAdmin):
    list_display = ('paciente', 'fisioterapeuta', 'data', 'hora')
    list_filter = ['data', 'fisioterapeuta']  
    search_fields = ['paciente__user__username', 'fisioterapeuta__user__username']

    def fisioterapeuta_display(self, obj):
        return obj.fisioterapeuta.user.username if obj.fisioterapeuta else "Não atribuído"
    fisioterapeuta_display.short_description = 'Fisioterapeuta'  
    
    list_display = ('paciente', 'fisioterapeuta_display', 'data', 'hora')

@admin.register(Disponibilidade)
class DisponibilidadeAdmin(admin.ModelAdmin):
    list_display = ('fisioterapeuta', 'dia_semana', 'horario_inicio', 'horario_fim')
    list_filter = ['fisioterapeuta', 'dia_semana']  
    search_fields = ['fisioterapeuta__user__username', 'dia_semana']  

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        return queryset.filter(fisioterapeuta__user=request.user) if not request.user.is_superuser else queryset
    
    def save_model(self, request, obj, form, change):
        if not obj.fisioterapeuta:
            obj.fisioterapeuta = Fisioterapeuta.objects.get(user=request.user)
        super().save_model(request, obj, form, change)