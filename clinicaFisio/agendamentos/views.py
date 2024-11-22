from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Agendamento, Disponibilidade
from .forms import AgendamentoForm
from usuarios.models import UserProfile

@login_required
def listar_agendamentos(request):
    paciente = UserProfile.objects.get(user=request.user)
    # Filtre os agendamentos pelo paciente
    agendamentos = Agendamento.objects.filter(paciente=paciente)
    return render(request, 'agendamentos/listar.html', {'agendamentos': agendamentos})

@login_required
def criar_agendamento(request):
    if request.method == 'POST':
        fisioterapeuta_id = request.POST.get('fisioterapeuta')
        data = request.POST.get('data')
        hora = request.POST.get('hora')

        fisioterapeuta = get_object_or_404(UserProfile, id=fisioterapeuta_id, tipo='Fisioterapeuta')
        paciente = UserProfile.objects.get(user=request.user)

        # Valide a disponibilidade do fisioterapeuta antes de criar o agendamento
        disponibilidade = Disponibilidade.objects.filter(
            fisioterapeuta=fisioterapeuta,
            dia_semana=data.strftime('%A').lower(),  # Dia da semana em inglês
            horario_inicio__lte=hora,
            horario_fim__gte=hora
        ).exists()

        if not disponibilidade:
            return render(request, 'agendamentos/criar.html', {
                'erro': 'Fisioterapeuta não disponível neste horário.',
                'fisioterapeutas': UserProfile.objects.filter(tipo='Fisioterapeuta')
            })

        # Cria o agendamento
        Agendamento.objects.create(
            paciente=paciente,
            fisioterapeuta=fisioterapeuta,
            data=data,
            hora=hora
        )
        return redirect('listar_agendamento')

    fisioterapeutas = UserProfile.objects.filter(tipo='Fisioterapeuta')
    return render(request, 'agendamentos/criar.html', {'fisioterapeutas': fisioterapeutas})

@login_required
def cancelar_agendamento(request, agendamento_id):
    agendamento = get_object_or_404(Agendamento, id=agendamento_id, paciente=request.user)
    agendamento.delete()
    return redirect('listar_agendamentos')

@login_required
def definir_disponibilidade(request):
    if request.method == "POST":
        dias = request.POST.getlist('dias')
        hora_inicio = request.POST.get('hora_inicio')
        hora_fim = request.POST.get('hora_fim')

        fisioterapeuta = UserProfile.objects.get(user=request.user)

        for dia in dias:
            Disponibilidade.objects.create(
                fisioterapeuta=fisioterapeuta,
                dia_semana=dia,  # Corrigido para 'dia_semana'
                horario_inicio=hora_inicio,  # Certifique-se de usar o nome correto
                horario_fim=hora_fim  # Certifique-se de usar o nome correto
            )
        return redirect('ver_consultas')

    return render(request, 'fisioterapeutas/definir_disponibilidade.html')

@login_required
def ver_consultas(request):
    fisioterapeuta = UserProfile.objects.get(user=request.user)
    consultas = Agendamento.objects.filter(fisioterapeuta=fisioterapeuta)
    return render(request, 'fisioterapeutas/ver_consultas.html', {'consultas': consultas})