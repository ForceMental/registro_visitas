from django.urls import path
from . import views

urlpatterns = [
    path('comunas/', views.ComunaListView.as_view(), name='comuna-list'),
    path('comunas/<int:pk>/', views.ComunaDetailView.as_view(), name='comuna-detail'),
]
