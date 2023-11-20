from django.urls import path
from . import views

urlpatterns = [
    path('clientes/', views.ClienteListView.as_view(), name='cliente-list'),
    path('clientes/create/', views.ClienteCreateView.as_view(), name='cliente-create'),
    path('clientes/update/<int:pk>/', views.ClienteUpdateView.as_view(), name='cliente-detail'),
    path('clientes/<int:pk>/', views.ClienteDetailView.as_view(), name='cliente-detail'),
]