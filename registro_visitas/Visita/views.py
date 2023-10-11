from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
import datetime
from rest_framework import status
from requests import Response
from rest_framework import generics
from .models import Visita
from .serializers import VisitaSerializer



# class VisitaPorFechaView(APIView):
#     def get(self, request, fecha, format=None):
#         try:
#             # Intenta convertir la cadena de fecha en un objeto de fecha
#             fecha_obj = datetime.strptime(fecha, '%Y-%m-%d').date()

#             # Filtra las visitas por la fecha proporcionada
#             visitas = Visita.objects.filter(fecha=fecha_obj)

#             # Serializa las visitas y devuelve la respuesta
#             serializer = VisitaSerializer(visitas, many=True)
#             return Response(serializer.data)
#         except ValueError:
#             # Si la cadena de fecha no es válida, devuelve una respuesta de error
#             return Response(
#                 {'error': 'Formato de fecha no válido. Utilice YYYY-MM-DD.'},
#                 status=status.HTTP_400_BAD_REQUEST
#             )

class VisitaListView(generics.ListCreateAPIView):
    queryset = Visita.objects.all()
    serializer_class = VisitaSerializer

class VisitaDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Visita.objects.all()
    serializer_class = VisitaSerializer
