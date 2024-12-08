from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from inventarioAPP.models import Paciente
from inventarioAPP.api.serializer import PacienteSerializer



class PacienteViewSet(viewsets.ModelViewSet):
    queryset = Paciente.objects.all()
    serializer_class = PacienteSerializer
    lookup_field = 'rut'
    permission_classes = []  

    # Buscar por estado
    @action(detail=False, methods=['get'])
    def estado_gripal(self, request):
        estado = request.query_params.get('estado', None)
        if estado:
            pacientes = Paciente.objects.filter(estado__icontains=estado)
            serializer = self.get_serializer(pacientes, many=True)
            return Response(serializer.data)
        return Response({"error": "Se requiere el parámetro 'estado'."}, status=400)

    # Buscar por RUT
    @action(detail=False, methods=['get'])
    def buscar_por_rut(self, request):
        rut = request.query_params.get('rut', None)
        if rut:
            try:
                paciente = Paciente.objects.get(rut=rut)  # Buscar por rut único
                serializer = self.get_serializer(paciente)
                return Response(serializer.data)
            except Paciente.DoesNotExist:
                return Response({"error": "Paciente no encontrado."}, status=404)
        return Response({"error": "Se requiere el parámetro 'rut'."}, status=400)
