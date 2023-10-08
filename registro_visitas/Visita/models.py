from django.db import models
from Cliente.models import Cliente
from Empleado.models import Empleado  # Asegúrate de importar correctamente desde tu otro proyecto si es necesario

class Visita(models.Model):
    TIPOS_VISITA = (
        ('F', 'En frío'),
        ('A', 'Agendada'),
    )

    ESTADOS_VISITA = (
        ('P', 'Pendiente'),
        ('R', 'Realizada'),
        ('C', 'Cancelada'),
    )

    tipo_visita = models.CharField(max_length=1, choices=TIPOS_VISITA, default='F')
    estado_visita = models.CharField(max_length=1, choices=ESTADOS_VISITA, default='P')
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.get_tipo_visita_display()} - {self.get_estado_visita_display()} - {self.cliente}"
