from django.db import models

from Comuna.models import Comuna

class Cliente(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    telefono = models.CharField(max_length=50)
    correo_electronico = models.EmailField(max_length=50)
    direccion = models.CharField(max_length=255)
    rut = models.CharField(max_length=12, unique=True)  # formato sin puntos y con guion, ej: 12345678-9
    comuna = models.ForeignKey(Comuna, on_delete=models.CASCADE, related_name="comunas")
    
    def __str__(self):
        return f"{self.nombre} {self.apellido}"
