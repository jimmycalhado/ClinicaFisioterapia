from django.db import models
from django.contrib.auth.models import User
from usuarios.models import Paciente, Fisioterapeuta


class Disponibilidade(models.Model):
    fisioterapeuta = models.ForeignKey(
        Fisioterapeuta,
        on_delete=models.CASCADE
    )
    dia_semana = models.CharField(
        max_length=20,
        choices=[
            ('segunda', 'Segunda-feira'),
            ('terca', 'Terça-feira'),
            ('quarta', 'Quarta-feira'),
            ('quinta', 'Quinta-feira'),
            ('sexta', 'Sexta-feira'),
            ('sabado', 'Sábado'),
            ('domingo', 'Domingo'),
        ]
    )
    horario_inicio = models.TimeField()
    horario_fim = models.TimeField()

    def __str__(self):
        return f"{self.fisioterapeuta.user.username} - {self.dia_semana} ({self.horario_inicio} às {self.horario_fim})"

    class Meta:
        unique_together = ('fisioterapeuta', 'dia_semana', 'horario_inicio')  # Evita horários duplicados para o mesmo fisioterapeuta e dia


class Agendamento(models.Model):
    paciente = models.ForeignKey(
        Paciente,
        on_delete=models.CASCADE,
        related_name='agendamentos'
    )
    fisioterapeuta = models.ForeignKey(
        Fisioterapeuta,
        on_delete=models.CASCADE,
        related_name='consultas',
        default=1
    )
    data = models.DateField()
    hora = models.TimeField()

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['fisioterapeuta', 'data', 'hora'],
                name='unique_fisioterapeuta_horario'
            )
        ]

    def __str__(self):
        return f"Agendamento de {self.paciente.user.username} com {self.fisioterapeuta.user.username} em {self.data} às {self.hora}"

    def salvar(self, *args, **kwargs):
        
        if Agendamento.objects.filter(fisioterapeuta=self.fisioterapeuta, data=self.data, hora=self.hora).exists():
            raise ValueError("Este horário já está ocupado.")
        super(Agendamento, self).save(*args, **kwargs)

