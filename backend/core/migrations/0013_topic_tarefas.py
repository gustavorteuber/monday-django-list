# Generated by Django 4.1.6 on 2023-02-02 04:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_topic_tarefas_lider'),
    ]

    operations = [
        migrations.AddField(
            model_name='topic',
            name='tarefas',
            field=models.ManyToManyField(to='core.tarefas'),
        ),
    ]
