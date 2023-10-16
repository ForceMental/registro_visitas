from django.db import models
from Region.models import Region

class Comuna(models.Model):
    nombre_comuna = models.CharField(max_length=255, unique=True)
    region = models.ForeignKey(Region, on_delete=models.CASCADE, related_name="comunas")

    def __str__(self):
        return self.nombre_comuna
