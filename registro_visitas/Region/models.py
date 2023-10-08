from django.db import models

class Region(models.Model):
    nombre_region = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre_region
