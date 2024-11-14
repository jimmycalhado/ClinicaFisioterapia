from django.db import models
from django.contrib.auth.models import User

class Agendamento(models.Model):
    paciente = models.ForeignKey(User, on_delete=models.CASCADE, related_name='agendamentos')
    data = models.DateField()
    horario = models.TimeField()
    descricao = models.TextField(blank=True, null=True)
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['data', 'horario']
        unique_together = ('data', 'horario')

    def __str__(self):
        return f"Consulta de {self.paciente.username} em {self.data} às {self.horario}"
