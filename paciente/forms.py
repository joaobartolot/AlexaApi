from django import forms
from django.contrib.auth.models import User

from .models import Paciente

class CreatePaciente(forms.ModelForm):
    class Meta:
        model = Paciente
        fields = [
            'nome',
            'endereco',
            'idade',
        ]
