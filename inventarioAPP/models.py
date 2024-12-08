from django.db import models

class Paciente(models.Model):
    rut = models.CharField(max_length=12, unique=True)  
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    fecha = models.DateField()
    hora_ingreso = models.TimeField()
    diagnostico = models.TextField()
    doctor = models.CharField(max_length=100)
    estado = models.CharField(max_length=50)  

    def __str__(self):
        return f"{self.apellidos}, {self.nombres} ({self.rut})"
