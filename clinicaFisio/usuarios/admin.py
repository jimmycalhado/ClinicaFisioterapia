from django.contrib import admin
from .models import UserProfile

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'cpf', 'telefone')
    search_fields = ('user__username', 'cpf')
    list_filter = ('user__is_active',)
    ordering = ('user__username',)
    readonly_fields = ('user',)
    
    # Permitir editar o CPF e o telefone
    fields = ('user', 'cpf', 'telefone')

# Registrar o modelo UserProfile no admin
admin.site.register(UserProfile, UserProfileAdmin)
