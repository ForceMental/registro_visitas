from django.urls import path
from . import views

urlpatterns = [
    path('visitas/<str:fecha>', views.VisitaListViewDate.as_view(), name='visita-list'),
    path('visitas/<int:pk>/', views.VisitaDetailView.as_view(), name='visita-detail'),
    path('visitas/', views.VisitaListView.as_view(), name='visita-list'),
    # path('visita_fecha>/<str:fecha>', views.VisitaPorFechaView.as_view(), name='visita-fecha'),

]