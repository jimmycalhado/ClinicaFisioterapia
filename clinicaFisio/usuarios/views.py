from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate as auth_login
from django.contrib.auth import logout
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.decorators import login_required
from django.urls import reverse, reverse_lazy
from django.contrib.auth.views import LoginView
from .forms import LoginForm, UserRegistrationForm
from django.views.generic.edit import CreateView
from .models import User

@user_passes_test(lambda u: u.is_superuser)
def cadastro_fisioterapeuta(request):
    if request.method == "GET":
        return render(request, 'cadastro_fisioterapeuta.html')
    else:
        username = request.POST.get('username')
        cpf = request.POST.get('cpf')
        telefone = request.POST.get('telefone')
        email = request.POST.get('email')
        senha = request.POST.get('senha')

        if User.objects.filter(cpf=cpf).exists():
            return HttpResponse('CPF já cadastrado')

        if User.objects.filter(email=email).exists():
            return HttpResponse('Email já cadastrado')

        user = User.objects.create_user(username=username, email=email, password=senha)
        User.objects.create(user=user, cpf=cpf, telefone=telefone)

        return HttpResponse('Fisioterapeuta cadastrado com sucesso!')


class Login(LoginView):
    form_class = LoginForm
    template_name = 'login.html'

    def form_valid(self, form):
        return super().form_valid(form)

    def form_invalid(self, form):
        return render(self.request, self.template_name, {
            'form': form,
            'error_message': form.errors['__all__'][0],
        })

    def get_success_url(self):
        return reverse('plataforma')

class Register(CreateView):
    template_name = 'cadastro.html'
    model = User
    form_class = UserRegistrationForm
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        user = form.save()
        return super().form_valid(form)

    def form_invalid(self, form):
        return render(self.request, self.template_name, {
            'form': form,
            'error_message': form.errors,
        })

@login_required(login_url="/login/")
def plataforma(request):
    cpf = request.user.cpf
    username = request.user.username
    return render(request, 'plataforma.html', {'username' : username, 'cpf' : cpf})

def logout_view(request):
    logout(request)
    return redirect('login')

