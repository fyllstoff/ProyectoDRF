from rest_framework import serializers
from inventarioAPP.models import Paciente

class PacienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paciente
        fields = [
            'id', 
            'rut', 
            'nombres', 
            'apellidos', 
            'fecha',  
            'hora_ingreso', 
            'diagnostico', 
            'doctor', 
            'estado'
        ]
