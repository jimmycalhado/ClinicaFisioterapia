from django.db import models
from django.contrib.auth.models import User

class Paciente(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    cpf = models.CharField(max_length=14, unique=True)
    telefone = models.CharField(max_length=15)

    def __str__(self):
        return f"Paciente: {self.user.username}"


class Fisioterapeuta(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    cpf = models.CharField(max_length=14, unique=True)
    telefone = models.CharField(max_length=15)
    registro_profissional = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return f"Fisioterapeuta: {self.user.username}"

