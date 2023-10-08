"""registro_visitas URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Cliente.views import ClienteListView, ClienteDetailView
from Region.views import RegionListView, RegionDetailView
from Comuna.views import ComunaListView, ComunaDetailView
from Empleado.views import EmpleadoListView, EmpleadoDetailView
from Visita.views import VisitaListView, VisitaDetailView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('clientes/', ClienteListView.as_view(), name='clientes-list'),
    path('clientes/<int:pk>/', ClienteDetailView.as_view(), name='cliente-detail'),
    path('comunas/', ComunaListView.as_view(), name='comuna-list'),
    path('comunas/<int:pk>/', ComunaDetailView.as_view(), name='comuna-detail'),
    path('regiones/', RegionListView.as_view(), name='region-list'),
    path('regiones/<int:pk>/', RegionDetailView.as_view(), name='region-detail'),
    path('empleados/', EmpleadoListView.as_view(), name='empleado-list'),
    path('empleados/<int:pk>/',EmpleadoDetailView.as_view(), name='empleado-detail'),
    path('visitas/', VisitaListView.as_view(), name='visita-list'),
    path('visitas/<int:pk>/', VisitaDetailView.as_view(), name='visita-detail'),
]
