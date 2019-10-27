from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Paciente(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    nome = models.CharField(max_length=100)
    endereco = models.CharField(max_length=200)
    idade = models.IntegerField()

    def __str__(self):
    	return f'{self.nome}'
