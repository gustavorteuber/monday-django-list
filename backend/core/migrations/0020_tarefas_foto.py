# Generated by Django 4.1.6 on 2023-02-04 01:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('uploader', '0001_initial'),
        ('core', '0019_alter_grupos_participantes_alter_tarefas_lider'),
    ]

    operations = [
        migrations.AddField(
            model_name='tarefas',
            name='foto',
            field=models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='uploader.image'),
        ),
    ]
