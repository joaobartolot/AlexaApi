from rest_framework import serializers

from paciente.models import Paciente
from medico.models import Medico, Consulta


class PacienteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Paciente
        fields = ['id', 'nome', 'endereco', 'idade']

class MedicoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Medico
        fields = ['id', 'crm', 'nome', 'endreco_consultorio']

class ConsultaSerializer(serializers.ModelSerializer):
    medico = serializers.PrimaryKeyRelatedField(many = False, read_only = True)
    paciente = serializers.PrimaryKeyRelatedField(many = False, read_only = True)

    class Meta:
        model = Consulta
        fields = ['paciente', 'medico', 'data']
