# Generated by Django 5.0.4 on 2024-11-21 20:37

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agendamentos', '0001_initial'),
        ('usuarios', '0004_userprofile_tipo_alter_userprofile_cpf_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='agendamento',
            options={},
        ),
        migrations.RenameField(
            model_name='agendamento',
            old_name='horario',
            new_name='hora',
        ),
        migrations.AlterUniqueTogether(
            name='agendamento',
            unique_together={('fisioterapeuta', 'data', 'hora')},
        ),
        migrations.AddField(
            model_name='agendamento',
            name='fisioterapeuta',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='consultas', to='usuarios.userprofile'),
        ),
        migrations.AlterField(
            model_name='agendamento',
            name='paciente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='agendamentos', to='usuarios.userprofile'),
        ),
        migrations.CreateModel(
            name='Disponibilidade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dia_semana', models.CharField(choices=[('segunda', 'Segunda-feira'), ('terca', 'Terça-feira'), ('quarta', 'Quarta-feira'), ('quinta', 'Quinta-feira'), ('sexta', 'Sexta-feira'), ('sabado', 'Sábado'), ('domingo', 'Domingo')], max_length=20)),
                ('horario_inicio', models.TimeField()),
                ('horario_fim', models.TimeField()),
                ('fisioterapeuta', models.ForeignKey(limit_choices_to={'userprofile__tipo': 'fisioterapeuta'}, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='agendamento',
            name='atualizado_em',
        ),
        migrations.RemoveField(
            model_name='agendamento',
            name='criado_em',
        ),
        migrations.RemoveField(
            model_name='agendamento',
            name='descricao',
        ),
    ]
