from django.urls import path
from . import views

urlpatterns = [
    path('regiones/', views.RegionListView.as_view(), name='region-list'),
    path('regiones/crear/', views.RegionCreateView.as_view(), name='region-create'),
    path('regiones/<int:pk>/', views.RegionDetailView.as_view(), name='region-detail'),
]
