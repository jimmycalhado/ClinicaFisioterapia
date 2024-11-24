from django.urls import path
from . import views

urlpatterns = [
    path('cadastro/', views.Register.as_view(), name='cadastro_paciente'),
    path('cadastro/fisioterapeuta/', views.cadastro_fisioterapeuta, name='cadastro_fisioterapeuta'),
    path('login/', views.Login.as_view(), name='login'),
    path('plataforma/', views.plataforma, name='plataforma'),
    path('logout/', views.logout_view, name='logout'),
]