from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission

class User(AbstractUser):
    telefone = models.CharField(max_length=15)
    cpf = models.CharField(max_length=14)

    groups = models.ManyToManyField(
        Group,
        related_name="custom_user_groups",  # Nome único para evitar conflitos
        blank=True
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name="custom_user_permissions",  # Nome único para evitar conflitos
        blank=True
    )
    
class Fisioterapeuta(User):
    telefone = models.CharField(max_length=15)
    cpf = models.CharField(max_length=14)

    groups = models.ManyToManyField(
        Group,
        related_name="custom_fisioterapeuta_groups",  # Nome único para evitar conflitos
        blank=True
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name="custom_fisioterapeuta_permissions",  # Nome único para evitar conflitos
        blank=True
    )

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"