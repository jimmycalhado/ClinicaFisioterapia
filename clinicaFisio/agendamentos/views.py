from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .models import Agendamento, Disponibilidade
from usuarios.models import Paciente, Fisioterapeuta
from datetime import datetime, timedelta

def is_fisioterapeuta(user):
    return Fisioterapeuta.objects.filter(user=user).exists()

@login_required
def listar_agendamentos(request):
    paciente = Paciente.objects.get(user=request.user)
    agendamentos = Agendamento.objects.filter(paciente=paciente)
    return render(request, 'agendamentos/listar.html', {'agendamentos': agendamentos})

@login_required
def criar_agendamento(request):
    if request.method == 'POST':
        fisioterapeuta_id = request.POST.get('fisioterapeuta')
        data = request.POST.get('data')
        hora = request.POST.get('hora')

        fisioterapeuta = get_object_or_404(Fisioterapeuta, id=fisioterapeuta_id)
        paciente = Paciente.objects.get(user=request.user)

        data_obj = datetime.strptime(data, "%Y-%m-%d")
        dia_semana = data_obj.strftime('%A').lower()

        disponibilidade = Disponibilidade.objects.filter(
            fisioterapeuta=fisioterapeuta,
            dia_semana=dia_semana,
            horario_inicio__lte=hora,
            horario_fim__gte=hora
        ).exists()

        if not disponibilidade:
            return render(request, 'agendamentos/criar.html', {
                'erro': 'Fisioterapeuta não disponível neste horário.',
                'fisioterapeutas': Fisioterapeuta.objects.all()
            })

        Agendamento.objects.create(
            paciente=paciente,
            fisioterapeuta=fisioterapeuta,
            data=data,
            hora=hora
        )
        return redirect('listar_agendamentos')

    fisioterapeutas = Fisioterapeuta.objects.all()
    return render(request, 'agendamentos/criar.html', {'fisioterapeutas': fisioterapeutas})

@login_required
def cancelar_agendamento(request, agendamento_id):
    agendamento = get_object_or_404(Agendamento, id=agendamento_id, paciente=request.user)
    agendamento.delete()
    return redirect('listar_agendamentos')

@login_required
def definir_disponibilidade(request):
    if not is_fisioterapeuta(request.user):
        return HttpResponse('Você precisa ser um fisioterapeuta para acessar essa página.')

    if request.method == "POST":
        dias = request.POST.getlist('dias')
        hora_inicio = request.POST.get('hora_inicio')
        hora_fim = request.POST.get('hora_fim')

        fisioterapeuta = Fisioterapeuta.objects.get(user=request.user)

        hora_inicio_obj = datetime.strptime(hora_inicio, '%H:%M')
        hora_fim_obj = datetime.strptime(hora_fim, '%H:%M')

        if (hora_fim_obj - hora_inicio_obj).seconds != 50 * 60:
            return HttpResponse('A duração da consulta deve ser de 50 minutos.')

        for dia in dias:
            Disponibilidade.objects.create(
                fisioterapeuta=fisioterapeuta,
                dia_semana=dia,
                horario_inicio=hora_inicio_obj.time(),
                horario_fim=hora_fim_obj.time()
            )
        return redirect('ver_consultas')

    return render(request, 'fisioterapeutas/definir_disponibilidade.html')

@login_required
def ver_consultas(request):
    if not is_fisioterapeuta(request.user):
        return HttpResponse('Você precisa ser um fisioterapeuta para acessar essa página.')

    fisioterapeuta = Fisioterapeuta.objects.get(user=request.user)
    consultas = Agendamento.objects.filter(fisioterapeuta=fisioterapeuta)
    return render(request, 'fisioterapeutas/ver_consultas.html', {'consultas': consultas})
