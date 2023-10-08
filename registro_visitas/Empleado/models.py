from django.db import models

class Empleado(models.Model):
    ROLES = (
        ('E', 'Ejecutivo'),
        ('J', 'Jefe'),
    )

    nombre_empleado = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    stock_disponible = models.PositiveIntegerField(default=0)
    tipo_empleado = models.CharField(max_length=1, choices=ROLES, default='E')
    empleado_jefe = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, related_name="subordinados", db_column='empleado_id_empleado')

    def __str__(self):
        return f"{self.nombre_empleado} {self.apellido}"
