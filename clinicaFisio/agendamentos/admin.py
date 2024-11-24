from django.contrib import admin
from .models import Agendamento, Fisioterapist
from usuarios.models import User


admin.site.register(User)
admin.site.register(Fisioterapist)
admin.site.register(Agendamento)