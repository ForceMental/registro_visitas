from rest_framework import serializers
from Comuna.models import Comuna
from Region.models import Region
from .models import Cliente

class ClienteSerializer(serializers.ModelSerializer):
    comuna = serializers.PrimaryKeyRelatedField(queryset=Comuna.objects.all(), required=True)
    region = serializers.PrimaryKeyRelatedField(source='comuna.region', queryset=Region.objects.all(), required=True)
    class Meta:
        model = Cliente
        fields = ['nombre', 'apellido', 'telefono', 'correo_electronico', 'direccion','rut', 'comuna', 'region']

class ClienteVisitaFrioSerializer(serializers.ModelSerializer):
    comuna = serializers.PrimaryKeyRelatedField(queryset=Comuna.objects.all(), required=True)
    region = serializers.PrimaryKeyRelatedField(source='comuna.region', queryset=Region.objects.all(), required=True)
    class Meta:
        model = Cliente
        fields = ['nombre', 'apellido', 'telefono', 'correo_electronico', 'direccion', 'comuna', 'region']
