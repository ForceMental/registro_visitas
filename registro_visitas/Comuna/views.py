from rest_framework import generics
from .models import Comuna
from .serializers import ComunaSerializer

class ComunaListView(generics.ListCreateAPIView):
    queryset = Comuna.objects.all()
    serializer_class = ComunaSerializer

class ComunaDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comuna.objects.all()
    serializer_class = ComunaSerializer
