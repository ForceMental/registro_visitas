from rest_framework import generics
from .models import Comuna
from .serializers import ComunaSerializer

class ComunaListView(generics.ListAPIView):
    queryset = Comuna.objects.all()
    serializer_class = ComunaSerializer


class ComunaCreateView(generics.CreateAPIView):
    queryset = Comuna.objects.all()
    serializer_class = ComunaSerializer


class ComunaDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comuna.objects.all()
    serializer_class = ComunaSerializer
