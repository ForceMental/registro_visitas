from rest_framework import serializers
from .models import Cliente

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'

class ClienteDetailSerializer(serializers.ModelSerializer):
    comuna = serializers.StringRelatedField()
    region = serializers.StringRelatedField(source='comuna.region')  # Asumiendo que hay una relación de comuna a región.

    class Meta:
        model = Cliente
        fields = ['nombre', 'apellido', 'telefono', 'correo_electronico', 'direccion', 'comuna', 'region']
