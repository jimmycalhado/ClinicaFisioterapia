from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate as auth_login
from django.contrib.auth import login as login_django, logout
from django.contrib.auth.decorators import login_required
from .models import UserProfile

def cadastro(request):
    if request.method == "GET":
        return render(request, 'cadastro.html')
    else:
        username = request.POST.get('username')
        cpf = request.POST.get('cpf')
        telefone = request.POST.get('telefone')
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        
        if UserProfile.objects.filter(cpf=cpf).exists():
            return HttpResponse('CPF já cadastrado')

        if User.objects.filter(email=email).exists():
            return HttpResponse('Email já cadastrado')
        
        user = User.objects.create_user(username=username, email=email, password=senha)
        UserProfile.objects.create(user=user, cpf=cpf, telefone=telefone)
        
        return HttpResponse('Usuário cadastrado com sucesso!')

def authenticate_with_cpf(cpf, password):
    try:
        # Buscar o perfil pelo CPF
        user_profile = UserProfile.objects.get(cpf=cpf)
        # Autenticar usando o username associado ao CPF encontrado
        user = auth_login(username=user_profile.user.username, password=password)
        return user
    except UserProfile.DoesNotExist:
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

@login_required(login_url="/login/")    
def plataforma(request):
    user_profile = UserProfile.objects.get(user=request.user)
    cpf = user_profile.cpf
    username = request.user.username
    return render(request, 'plataforma.html', {'username' : username, 'cpf' : cpf})

def logout_view(request):
    logout(request)
    return redirect('login')