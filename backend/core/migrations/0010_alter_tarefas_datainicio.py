# Generated by Django 4.1.6 on 2023-02-02 03:16

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_rename_ultima_grupos_criado_rename_fim_tarefas_prazo_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tarefas',
            name='datainicio',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
