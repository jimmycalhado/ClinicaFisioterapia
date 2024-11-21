from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    cpf = models.CharField(max_length=14, unique=True)
    telefone = models.CharField(max_length=15)
    tipo = models.CharField(
        max_length=20,
        choices=[('paciente', 'Paciente'), ('fisioterapeuta', 'Fisioterapeuta')],
        default='paciente',  
    )

    def __str__(self):
        return self.user.username
