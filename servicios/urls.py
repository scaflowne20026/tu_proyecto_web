from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('servicio/<int:pk>/', views.detalle_servicio, name='detalle_servicio'),
]
