from django.shortcuts import render, get_object_or_404
from .models import Servicio

def inicio(request):
    servicios = Servicio.objects.all()
    return render(request, 'inicio.html', {'servicios': servicios})

def detalle_servicio(request, pk):
    servicio = get_object_or_404(Servicio, pk=pk)
    return render(request, 'servicio_detalle.html', {'servicio': servicio})
