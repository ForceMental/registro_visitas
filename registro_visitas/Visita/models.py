from django.utils import timezone
from django.db import models
from Cliente.models import Cliente

class Visita(models.Model):
    TIPOS_VISITA = (
        ('F', 'En frío'),
        ('A', 'Agendada'),
    )

    tipo_visita = models.CharField(max_length=1, choices=TIPOS_VISITA, default='F')
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    empleado_id = models.CharField(max_length=255, default='') 
    empleado_nombre = models.CharField(max_length=255)
    fecha_visita = models.DateTimeField(default=timezone.now)
    reprogramada = models.BooleanField(default=False)  # Indica si la visita ha sido reprogramada
    contador_reprogramaciones = models.IntegerField(default=0)
    finalizada = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.get_tipo_visita_display()} - {self.cliente}"
    

