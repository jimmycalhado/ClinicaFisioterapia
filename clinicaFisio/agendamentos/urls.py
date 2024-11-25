from django.urls import path
from . import views

urlpatterns = [
    path('listar/', views.listar_agendamentos, name='listar_agendamentos'),
    path('criar/', views.agendar_consulta, name='criar_agendamento'),
    path('cancelar/<int:agendamento_id>/', views.cancelar_agendamento, name='cancelar_agendamento'),
    path('definir_disponibilidade/', views.definir_disponibilidade, name='definir_disponibilidade'),
    path('ver_consultas/', views.ver_consultas, name='ver_consultas'),
]