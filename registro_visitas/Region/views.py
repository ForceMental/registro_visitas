from rest_framework import generics
from .models import Region
from .serializers import RegionSerializer

class RegionListView(generics.ListCreateAPIView):
    queryset = Region.objects.all()
    serializer_class = RegionSerializer

class RegionDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Region.objects.all()
    serializer_class = RegionSerializer
