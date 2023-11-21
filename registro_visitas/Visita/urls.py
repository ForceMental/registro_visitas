from django.urls import path
from . import views

urlpatterns = [
    path('visitasIdFecha/', views.VisitaListViewDate.as_view(), name='visita-list'),
    path('visitas/<int:pk>/', views.VisitaDetailView.as_view(), name='visita-detail'),
    path('visitas/', views.VisitaListView.as_view(), name='visita-list'),
    path('reprogramar/<int:pk>/', views.ReprogramarVisitaView.as_view(), name='reprogramar-visita'),
    # path('visita_fecha>/<str:fecha>', views.VisitaPorFechaView.as_view(), name='visita-fecha'),
    path('visita/<int:pk>/finalizar/', views.finalizar_visita, name='finalizar_visita'),
    path('visita/<int:pk>/cancelar/', views.cancelar_visita, name='cancelar_visita'),

]