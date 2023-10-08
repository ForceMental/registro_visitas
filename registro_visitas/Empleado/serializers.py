from rest_framework import serializers
from .models import Empleado


class EmpleadoSerializer(serializers.ModelSerializer):
    empleado_jefe_id = serializers.IntegerField(write_only=True, required=False, allow_null=True)

    class Meta:
        model = Empleado
        fields = '__all__'
        
    def create(self, validated_data):
        empleado_jefe_id = validated_data.pop('empleado_jefe_id', None)
        
        if empleado_jefe_id:
            try:
                empleado_jefe = Empleado.objects.get(pk=empleado_jefe_id)
                validated_data['empleado_jefe'] = empleado_jefe
            except Empleado.DoesNotExist:
                raise serializers.ValidationError("El jefe con el ID proporcionado no existe.")
        
        return super(EmpleadoSerializer, self).create(validated_data)
