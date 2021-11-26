from django.db import models

# Create your models here.

class Professor(models.Model):
    nome = models.CharField(max_length=30)
    disciplina = models.CharField(max_length=30)
    registro = models.CharField(max_length=10)


class Aluno(models.Model):
    nome = models.CharField(max_length=30)
    turma = models.CharField(max_length=10)
    serie = models.IntegerField()
    cgm = models.CharField(max_length=10)