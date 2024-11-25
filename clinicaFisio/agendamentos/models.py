from django.db import models
from usuarios.models import User, Fisioterapeuta
from django.db.models import UniqueConstraint


#class Fisioterapist(models.Model):
   #id = models.AutoField(primary_key=True)
   #user = models.OneToOneField(User, on_delete=models.PROTECT)
   #email = models.EmailField(unique=True)
   #telefone= models.CharField(max_length=15, null=True, blank=True)


class Agendamento(models.Model):
    paciente = models.ForeignKey(User, on_delete=models.CASCADE, related_name='agendamentos')
    fisioterapeuta = models.ForeignKey(Fisioterapeuta, on_delete=models.CASCADE, related_name='consultas', null=True, blank=True)
    data = models.DateField()
    hora = models.TimeField()

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['fisioterapeuta', 'data', 'hora'], name='unique_fisioterapeuta_horario')
        ]

    def __str__(self):
        return f"Agendamento de {self.paciente} com {self.fisioterapeuta} em {self.data} às {self.hora}"

class Disponibilidade(models.Model):
    fisioterapeuta = models.ForeignKey(
        Fisioterapeuta,
        on_delete=models.CASCADE,
 )
    dia_semana = models.CharField(max_length=20, choices=[
        ('segunda', 'Segunda-feira'),
        ('terca', 'Terça-feira'),
        ('quarta', 'Quarta-feira'),
        ('quinta', 'Quinta-feira'),
        ('sexta', 'Sexta-feira'),
        ('sabado', 'Sábado'),
        ('domingo', 'Domingo'),
    ])
    horario_inicio = models.TimeField()
    horario_fim = models.TimeField()

    def __str__(self):
        return f"{self.fisioterapeuta.user.username} - {self.dia_semana} ({self.horario_inicio} às {self.horario_fim})"

