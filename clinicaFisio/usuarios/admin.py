from django.contrib import admin
from .models import UserProfile

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'cpf', 'telefone', 'tipo',)
    search_fields = ('user__username', 'cpf')
    list_filter = ('user__is_active',)
    ordering = ('user__username',)
    readonly_fields = ('user',)
    
    fields = ('user', 'cpf', 'telefone')


