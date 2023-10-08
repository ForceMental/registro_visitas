from rest_framework import serializers, exceptions
from .models import Visita
from Cliente.models import Cliente
from Cliente.serializers import ClienteSerializer
from Empleado.serializers import EmpleadoSerializer  # Asegúrate de tener un serializador para Empleado
from Comuna.serializers import ComunaSerializer
from Region.serializers import RegionSerializer

class VisitaSerializer(serializers.ModelSerializer):
    cliente = ClienteSerializer(read_only=True)
    cliente_id = serializers.IntegerField(write_only=True)
    empleado = EmpleadoSerializer(read_only=True)
    comuna = ComunaSerializer(source="cliente.comuna", read_only=True)
    region = RegionSerializer(source="cliente.comuna.region", read_only=True)
    empleado_id = serializers.IntegerField(write_only=True)


    class Meta:
        model = Visita
        fields = ['id', 'tipo_visita', 'estado_visita', 'cliente', 'empleado', 'comuna', 'region', 'cliente_id', 'empleado_id']
        
        
from Empleado.models import Empleado  # Importamos el modelo Empleado para poder hacer la consulta

def create(self, validated_data):
    # Manejo del cliente_id
    cliente_id = validated_data.pop('cliente_id', None)
    
    if not cliente_id:
        raise exceptions.ValidationError("El campo 'cliente_id' es requerido.")
        
    try:
        cliente = Cliente.objects.get(pk=cliente_id)
    except Cliente.DoesNotExist:
        raise exceptions.ValidationError("El cliente con el ID proporcionado no existe.")
        
    validated_data['cliente'] = cliente
    
    # Manejo del empleado_id
    empleado_id = validated_data.pop('empleado_id', None)  # Extraemos el empleado_id
    
    if not empleado_id:
        raise exceptions.ValidationError("El campo 'empleado_id' es requerido.")
    
    try:
        empleado = Empleado.objects.get(pk=empleado_id)
    except Empleado.DoesNotExist:
        raise exceptions.ValidationError("El empleado con el ID proporcionado no existe.")
    
    if empleado.tipo_empleado != 'E':
        raise exceptions.ValidationError("Solo los empleados tipo 'E' pueden crear visitas.")
    
    validated_data['empleado'] = empleado
    
    return super(VisitaSerializer, self).create(validated_data)
