from rest_framework import serializers, exceptions
from .models import Visita
from Cliente.models import Cliente
from Cliente.serializers import ClienteVisitaFrioSerializer  
from Comuna.serializers import ComunaSerializer
from Region.serializers import RegionSerializer

class VisitaSerializer(serializers.ModelSerializer):
    cliente = ClienteVisitaFrioSerializer(read_only=True)
    cliente_id = serializers.IntegerField(write_only=True)
    empleado_id = serializers.IntegerField(write_only=True)


    class Meta:
        model = Visita
        fields = ['id', 'tipo_visita', 'cliente', 'cliente_id', 'empleado_id']
        
        

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
    

    
    return super(VisitaSerializer, self).create(validated_data)
