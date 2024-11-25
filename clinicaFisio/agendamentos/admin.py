from django.contrib import admin
from .models import Agendamento
from usuarios.models import User,  Fisioterapeuta


admin.site.register(User)
admin.site.register(Agendamento)