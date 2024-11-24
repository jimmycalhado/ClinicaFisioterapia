from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate as auth_login
from django.contrib.auth import login as login_django, logout
from django.contrib.auth.decorators import user_passes_test, login_required
from .models import Paciente, Fisioterapeuta

def cadastro_paciente(request):
    if request.method == "POST":
        username = request.POST.get('username')
        cpf = request.POST.get('cpf')
        telefone = request.POST.get('telefone')
        email = request.POST.get('email')
        senha = request.POST.get('senha')

        # Verificando se o CPF já foi cadastrado
        if Paciente.objects.filter(cpf=cpf).exists():
            return HttpResponse('CPF já cadastrado')

        if User.objects.filter(email=email).exists():
            return HttpResponse('Email já cadastrado')

        # Criar o usuário e associar com o paciente
        user = User.objects.create_user(username=username, email=email, password=senha)
        Paciente.objects.create(user=user, cpf=cpf, telefone=telefone)

        return HttpResponse('Paciente cadastrado com sucesso!')
    
    return render(request, 'cadastro.html')

@user_passes_test(lambda u: u.is_superuser) 
def cadastro_fisioterapeuta(request):
    if request.method == "POST":
        username = request.POST.get('username')
        cpf = request.POST.get('cpf')
        telefone = request.POST.get('telefone')
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        registro_profissional = request.POST.get('registro_profissional')

        # Verificando se o CPF ou Registro Profissional já foi cadastrado
        if Fisioterapeuta.objects.filter(cpf=cpf).exists():
            return HttpResponse('CPF já cadastrado')

        if User.objects.filter(email=email).exists():
            return HttpResponse('Email já cadastrado')

        if Fisioterapeuta.objects.filter(registro_profissional=registro_profissional).exists():
            return HttpResponse('Registro profissional já cadastrado')

        # Criar o usuário e associar com o fisioterapeuta
        user = User.objects.create_user(username=username, email=email, password=senha)
        Fisioterapeuta.objects.create(user=user, cpf=cpf, telefone=telefone, registro_profissional=registro_profissional)

        return HttpResponse('Fisioterapeuta cadastrado com sucesso!')
    
    return render(request, 'cadastro_fisioterapeuta.html')

def authenticate_with_cpf(cpf, password):
    try:
        # Buscar em Paciente ou Fisioterapeuta
        user_profile = Paciente.objects.filter(cpf=cpf).first() or Fisioterapeuta.objects.filter(cpf=cpf).first()
        if user_profile:
            user = auth_login(username=user_profile.user.username, password=password)
            return user
        return None
    except Exception:
        return None

def login(request):
    if request.method == "GET":
        return render(request, 'login.html')
    else:
        cpf = request.POST.get('cpf')
        senha = request.POST.get('senha')
        
        user = authenticate_with_cpf(cpf, senha)
        
        if user:
            login_django(request, user) 
            return redirect('plataforma')
        else:
            return HttpResponse('CPF ou senha inválido')

@login_required
def plataforma(request):
    # Buscar em Paciente ou Fisioterapeuta
    user_profile = (
        Paciente.objects.filter(user=request.user).first()
        or Fisioterapeuta.objects.filter(user=request.user).first()
    )
    if user_profile:
        cpf = user_profile.cpf
        username = request.user.username
        return render(request, 'plataforma.html', {'username': username, 'cpf': cpf})
    else:
        return HttpResponse('Erro ao carregar dados do usuário')

def logout_view(request):
    logout(request)
    return redirect('login')

