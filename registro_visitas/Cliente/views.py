from rest_framework.views import APIView
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics
from .models import Cliente
from .serializers import ClienteSerializer, ClienteCreateSerializer

class ClienteCreateView(generics.CreateAPIView):
    queryset = Cliente.objects.all()
    serializer_class = ClienteCreateSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        # Verificar que todos los campos requeridos estén presentes
        required_fields = ['nombre', 'apellido', 'telefono', 'correo_electronico', 'direccion', 'comuna', 'rut']
        missing_fields = [field for field in required_fields if field not in request.data]

        if missing_fields:
            errors = {field: ['Este campo es requerido.'] for field in missing_fields}
            return Response(errors, status=status.HTTP_400_BAD_REQUEST)

        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
class ClienteListView(generics.ListCreateAPIView):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

class ClienteDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer