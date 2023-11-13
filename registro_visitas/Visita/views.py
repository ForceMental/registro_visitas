from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from datetime import datetime
from rest_framework.response import Response
from django.utils.dateparse import parse_datetime
from django.utils import timezone

from rest_framework import status
from rest_framework import generics
from .models import Visita
from .serializers import VisitaSerializer
from rest_framework.exceptions import ParseError


class VisitaListViewDate(generics.ListAPIView):
    serializer_class = VisitaSerializer

    def get_queryset(self):
        fecha_str = self.request.query_params.get('fecha', None)
        empleado_id = self.request.query_params.get('id_empleado', None)

        queryset = Visita.objects.all()

        if fecha_str:
            try:
                fecha = datetime.strptime(fecha_str, '%d-%m-%Y')
                queryset = queryset.filter(fecha_visita__date=fecha)
            except ValueError:
                pass

        if empleado_id:
            queryset = queryset.filter(empleado_id=empleado_id)

        return queryset

class ReprogramarVisitaView(APIView):

    def patch(self, request, pk):
        fecha_nueva_str = request.data.get('fecha_visita')
        visita = get_object_or_404(Visita, pk=pk)
        
        # Validate and parse new date
        fecha_con_hora = self._parse_fecha_nueva(fecha_nueva_str)
        if isinstance(fecha_con_hora, Response):
            return fecha_con_hora

        # Perform update
        return self._update_visita(visita, fecha_con_hora)

    def _parse_fecha_nueva(self, fecha_nueva_str):
        if not fecha_nueva_str:
            return Response(
                {"message": "Debe proporcionar una nueva fecha para reprogramar la visita."},
                status=status.HTTP_400_BAD_REQUEST
            )

        try:
            fecha_nueva = datetime.strptime(fecha_nueva_str, '%d-%m-%Y').date()
            return timezone.make_aware(datetime.combine(fecha_nueva, datetime.min.time()))
        except ValueError:
            return Response(
                {"message": "Formato de fecha inválido. Debe ser DD-MM-YYYY."},
                status=status.HTTP_400_BAD_REQUEST
            )

    def _update_visita(self, visita, fecha_con_hora):
        visita.fecha_visita = fecha_con_hora
        visita.contador_reprogramaciones += 1
        visita.reprogramada = True
        visita.save(update_fields=['fecha_visita', 'contador_reprogramaciones', 'reprogramada'])

        serializer = VisitaSerializer(visita)
        return Response(serializer.data, status=status.HTTP_200_OK)
    

class VisitaListView(generics.ListCreateAPIView):
    queryset = Visita.objects.all()
    serializer_class = VisitaSerializer

class VisitaDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Visita.objects.all()
    serializer_class = VisitaSerializer
