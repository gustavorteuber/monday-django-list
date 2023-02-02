from django.contrib.auth.models import AbstractUser
from uploader.models import Image
from django.db import models
from django.utils import timezone




class Usuario(AbstractUser):
    foto = models.ForeignKey(
        Image,
        related_name="+",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        default="",
    )

class Grupos(models.Model):
    Nome = models.CharField(max_length=200, blank=True)
    Participantes = models.ManyToManyField(Usuario)
    Criado = models.DateTimeField(default=timezone.now)
    Alterado = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.Nome


class Tarefas(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.TextField()
    datainicio = models.DateTimeField(default=timezone.now)
    prazofinal = models.DateTimeField(default=timezone.now)
    lider = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    grupo = models.ForeignKey(Grupos, on_delete=models.CASCADE)
    Entregue = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.titulo


class Topic(models.Model):
    titulo = models.CharField(max_length=50)

    def __str__(self):
        return self.titulo

class conjTopic(models.Model):
    Topico = models.ManyToManyField(Topic)
    Tarefa = models.ManyToManyField(Tarefas)

    def __str__(self):
        return self.Tarefa


