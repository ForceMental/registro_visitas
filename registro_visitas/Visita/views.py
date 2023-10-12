from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from datetime import datetime

from rest_framework import status
from requests import Response
from rest_framework import generics
from .models import Visita
from .serializers import VisitaSerializer

class VisitaListViewDate(generics.ListAPIView):
    serializer_class = VisitaSerializer

    def get_queryset(self):
        fecha_str = self.kwargs.get('fecha', None)
        
        if fecha_str:
            try:
                # Analiza la fecha desde la URL en el formato "DD-MM-YYYY"
                fecha = datetime.strptime(fecha_str, '%d-%m-%Y')
                
                # Filtra las visitas por la fecha
                return Visita.objects.filter(fecha_visita__date=fecha)
            except ValueError:
                pass  # Manejar errores de formato de fecha aquí si es necesario
        
        return Visita.objects.none()  



class VisitaListView(generics.ListCreateAPIView):
    queryset = Visita.objects.all()
    serializer_class = VisitaSerializer

class VisitaDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Visita.objects.all()
    serializer_class = VisitaSerializer
