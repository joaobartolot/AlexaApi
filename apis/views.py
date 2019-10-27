from django.contrib.auth.models import User
from rest_framework.views import APIView, Response
from rest_framework import authentication, permissions

from paciente.models import Paciente
from medico.models import Medico, Consulta
from .serializers import PacienteSerializer, MedicoSerializer, ConsultaSerializer

# Create your views here.

class PacienteLista(APIView):

    def get(self, request, format='json'):
        pacientes = Paciente.objects.all()

        serializer = PacienteSerializer(pacientes, many=True)

        return Response(serializer.data)

class MedicoLista(APIView):
    
    def get(self, request, format=None):
        medico = Medico.objects.all()

        serializer = MedicoSerializer(medico, many=True)

        return Response(serializer.data)

class ConsultaLista(APIView):
    
    def get(self, request, format=None):
        consulta = Consulta.objects.all()

        serializer = ConsultaSerializer(consulta, many=True)

        return Response(serializer.data)
