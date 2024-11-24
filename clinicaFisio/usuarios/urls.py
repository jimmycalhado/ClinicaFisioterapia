from django.urls import path
from . import views

urlpatterns = [
    path('cadastro/' , views.cadastro_paciente, name='cadastro_paciente'),
    path('cadastro/fisioterapeuta/', views.cadastro_fisioterapeuta, name='cadastro_fisioterapeuta'),
    path('' , views.login, name='login'),
    path( 'plataforma/' , views.plataforma, name='plataforma'),
    path('logout/', views.logout_view, name='logout'),
]