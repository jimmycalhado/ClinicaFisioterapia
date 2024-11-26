from django import forms
from .models import User
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from agendamentos.models import Agendamento, Fisioterapist


class LoginForm(AuthenticationForm):
    username = forms.CharField(
        label='Username',
        max_length=150,
        widget=forms.TextInput(attrs={
            'class': 'block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 placeholder:pl-2 focus:ring-2 focus:ring-inset focus:ring-green-600 sm:text-sm/6',
            'placeholder': 'Insira seu nome de usuário',
        })
    )
    password = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(attrs={
            'class': 'block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 placeholder:pl-2 focus:ring-2 focus:ring-inset focus:ring-green-600 sm:text-sm/6',
            'placeholder': 'Insira sua senha',
        })
    )


class UserRegistrationForm(UserCreationForm):
    password1 = forms.CharField(
        label="Senha",
        widget=forms.PasswordInput(attrs={
            'class': 'block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 placeholder:pl-2 focus:ring-2 focus:ring-inset focus:ring-green-600 sm:text-sm/6',
            'placeholder': 'Senha',
            'id': 'password1',
        })
    )
    password2 = forms.CharField(
        label="Confirme a Senha",
        widget=forms.PasswordInput(attrs={
            'class': 'block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 placeholder:pl-2 focus:ring-2 focus:ring-inset focus:ring-green-600 sm:text-sm/6',
            'placeholder': 'Confirme a Senha',
            'id': 'password2',
        })
    )

    class Meta:
        model = User
        fields = [
            'first_name', 'last_name', 'username', 'cpf', 'email', 'telefone',
            'password1', 'password2',
        ]
        widgets = {
            'first_name': forms.TextInput(attrs={
                'class': 'block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 placeholder:pl-2 focus:ring-2 focus:ring-inset focus:ring-green-600 sm:text-sm/6',
                'placeholder': 'Primeiro Nome',
                'id': 'nome',
            }),
            'last_name': forms.TextInput(attrs={
                'class': 'block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 placeholder:pl-2 focus:ring-2 focus:ring-inset focus:ring-green-600 sm:text-sm/6',
                'placeholder': 'Sobrenome',
                'id': 'sobrenome',
            }),
            'username': forms.TextInput(attrs={
                'class': 'block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 placeholder:pl-2 focus:ring-2 focus:ring-inset focus:ring-green-600 sm:text-sm/6',
                'placeholder': 'Nome de Usuário',
                'id': 'nome_usuario',
            }),
            'cpf': forms.TextInput(attrs={
                'class': 'block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 placeholder:pl-2 focus:ring-2 focus:ring-inset focus:ring-green-600 sm:text-sm/6',
                'placeholder': '000.000.000-00',
                'maxlength': '14',
                'id': 'CPF',
                'inputmode': 'numeric',
            }),
            'email': forms.EmailInput(attrs={
                'class': 'block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 placeholder:pl-2 focus:ring-2 focus:ring-inset focus:ring-green-600 sm:text-sm/6',
                'placeholder': 'Email',
                'id': 'email',
            }),
            'telefone': forms.TextInput(attrs={
                'class': 'block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 placeholder:pl-2 focus:ring-2 focus:ring-inset focus:ring-green-600 sm:text-sm/6',
                'placeholder': '(XX) 9XXXX-XXXX',
                'maxlength': '15',
                'id': 'telefone',
                'inputmode': 'tel',
            }),
        }

class AgendamentoForm(forms.ModelForm):
    class Meta:
        model = Agendamento
        fields = ['fisioterapeuta', 'data', 'hora']
        widgets = {
            'fisioterapeuta': forms.Select(attrs={'class': 'form-select mt-2 mb-2'}),
            'data': forms.DateInput(attrs={'type': 'date', 'class': 'mt-3 mb-3'}),  
            'hora': forms.TimeInput(attrs={'type': 'time'}),
            }