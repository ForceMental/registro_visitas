from rest_framework import serializers
from Comuna.models import Comuna
from Region.models import Region
from Comuna.serializers import ComunaSerializer
from Region.serializers import RegionSerializer
from .models import Cliente

class ClienteSerializer(serializers.ModelSerializer):
    comuna = serializers.PrimaryKeyRelatedField(source='comuna.nombre_comuna', queryset=Comuna.objects.all(), required=True)
    region = serializers.PrimaryKeyRelatedField(source='comuna.region.nombre_region', queryset=Region.objects.all(), required=True)
    class Meta:
        model = Cliente
        fields = ['id', 'nombre', 'apellido', 'telefono', 'correo_electronico', 'direccion', 'rut', 'comuna', 'region']
# def create(self, validated_data):
#     comuna_data = validated_data.pop('comuna')
#     region_data = comuna_data.pop('region')

#     # Primero verifica si la Región ya existe
#     region_instance, _ = Region.objects.get_or_create(nombre_region=region_data['nombre_region'])

#     # Luego verifica si la Comuna ya existe
#     comuna_instance, _ = Comuna.objects.get_or_create(nombre_comuna=comuna_data['nombre_comuna'], region=region_instance)

#     # Finalmente, crea el Cliente con la Comuna (ya sea la existente o la nueva)
#     cliente_instance = Cliente.objects.create(comuna=comuna_instance, **validated_data)
#     return cliente_instance


class ClienteVisitaFrioSerializer(serializers.ModelSerializer):
    comuna = serializers.PrimaryKeyRelatedField(source='comuna.nombre_comuna', queryset=Comuna.objects.all(), required=True)
    region = serializers.PrimaryKeyRelatedField(source='comuna.region.nombre_region', queryset=Region.objects.all(), required=True)
    class Meta:
        model = Cliente
        fields = ['nombre', 'apellido', 'telefono', 'correo_electronico', 'direccion', 'comuna', 'region']

class ClienteCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = ['nombre', 'apellido', 'telefono', 'correo_electronico', 'direccion', 'comuna', 'rut']