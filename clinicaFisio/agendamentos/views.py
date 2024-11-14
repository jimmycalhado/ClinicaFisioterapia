from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Agendamento
from .forms import AgendamentoForm

@login_required
def listar_agendamentos(request):
    agendamentos = Agendamento.objects.filter(paciente=request.user)
    return render(request, 'agendamentos/listar.html', {'agendamentos': agendamentos})

@login_required
def criar_agendamento(request):
    if request.method == 'POST':
        form = AgendamentoForm(request.POST)
        if form.is_valid():
            agendamento = form.save(commit=False)
            agendamento.paciente = request.user
            agendamento.save()
            return redirect('listar_agendamentos')
    else:
        form = AgendamentoForm()
    return render(request, 'agendamentos/criar.html', {'form': form})

@login_required
def cancelar_agendamento(request, agendamento_id):
    agendamento = get_object_or_404(Agendamento, id=agendamento_id, paciente=request.user)
    agendamento.delete()
    return redirect('listar_agendamentos')
