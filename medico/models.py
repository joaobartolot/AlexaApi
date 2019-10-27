from django.db import models
from django.contrib.auth.models import User

from paciente.models import Paciente

# Create your models here.

class Medico(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    crm = models.IntegerField()
    nome = models.CharField(max_length=100)
    endreco_consultorio = models.CharField(max_length=250)
    especialidade = models.CharField(max_length=100)

    def __str__(self):
    	return f'{self.nome}'

class Consulta(models.Model):
    medico = models.ForeignKey(Medico, on_delete = models.CASCADE)
    paciente = models.ForeignKey(Paciente, on_delete = models.CASCADE, null = True)

    data = models.DateField()
