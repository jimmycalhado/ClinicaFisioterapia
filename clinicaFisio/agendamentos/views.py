from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Agendamento, Disponibilidade
from usuarios.forms import AgendamentoForm
from usuarios.models import User,  Fisioterapeuta

@login_required
def listar_agendamentos(request):
    paciente = request.user
    agendamentos = Agendamento.objects.filter(paciente=paciente)
    return render(request, 'agendamentos/listar.html', {'agendamentos': agendamentos})

@login_required
def agendar_consulta(request):
    if request.method == 'POST':
        form = AgendamentoForm(request.POST)
        if form.is_valid():
            fisioterapeuta = form.cleaned_data['fisioterapeuta']
            data = form.cleaned_data['data']
            hora = form.cleaned_data['hora']
            Agendamento.objects.create(
                paciente=request.user,
                fisioterapeuta=fisioterapeuta,
                data=data,
                hora=hora
            )
            return redirect('plataforma')  # Redireciona para uma página de sucesso
    else:
        form = AgendamentoForm()

    fisioterapeuta = Fisioterapeuta.objects.all()
    return render(request, 'agendamentos/criar.html', {'form': form, 'fisioterapists': fisioterapeuta})

@login_required(login_url='login')
def cancelar_agendamento(request, agendamento_id):
    agendamento = get_object_or_404(Agendamento, id=agendamento_id, paciente=request.user)
    agendamento.delete()
    return redirect('listar_agendamentos')

@login_required(login_url='login')
def definir_disponibilidade(request):
    if request.method == "POST":
        dias = request.POST.getlist('dias')
        hora_inicio = request.POST.get('hora_inicio')
        hora_fim = request.POST.get('hora_fim')

        fisioterapeuta = User.objects.get(user=request.user)

        for dia in dias:
            Disponibilidade.objects.create(
                fisioterapeuta=fisioterapeuta,
                dia_semana=dia,  # Corrigido para 'dia_semana'
                horario_inicio=hora_inicio,  # Certifique-se de usar o nome correto
                horario_fim=hora_fim  # Certifique-se de usar o nome correto
            )
        return redirect('ver_consultas')

    return render(request, 'fisioterapeutas/definir_disponibilidade.html')

@login_required(login_url='login')
def ver_consultas(request):
    fisioterapeuta = User.objects.get(user=request.user)
    consultas = Agendamento.objects.filter(fisioterapeuta=fisioterapeuta)
    return render(request, 'fisioterapeutas/ver_consultas.html', {'consultas': consultas})