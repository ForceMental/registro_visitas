from django.shortcuts import render
from rest_framework import generics
from .models import Cliente
from .serializers import ClienteSerializer, ClienteDetailSerializer

class ClienteListView(generics.ListCreateAPIView):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

class ClienteDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

class ClienteDetailView(generics.RetrieveAPIView):
    queryset = Cliente.objects.all()
    serializer_class = ClienteDetailSerializer