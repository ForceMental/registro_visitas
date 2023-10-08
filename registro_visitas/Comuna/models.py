from django.db import models
from Cliente.models import Cliente
from Region.models import Region

class Comuna(models.Model):
    nombre_comuna = models.CharField(max_length=255)
    cliente = models.OneToOneField(Cliente, on_delete=models.SET_NULL, null=True, related_name="comuna")
    region = models.ForeignKey(Region, on_delete=models.CASCADE, related_name="comunas")

    def __str__(self):
        return self.nombre_comuna
