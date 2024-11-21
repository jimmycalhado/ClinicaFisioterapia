from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('' , include('usuarios.urls')),
    path('agendamentos/', include('agendamentos.urls')),

    path("__reload__/", include("django_browser_reload.urls")),
]
