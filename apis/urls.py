from django.urls import path, include
from rest_framework import routers
from .views import PacienteLista, MedicoLista, ConsultaLista

urlpatterns = [
    path('paciente/', PacienteLista.as_view()),
    path('medico/', MedicoLista.as_view()),
    path('consulta/', ConsultaLista.as_view()),
]
