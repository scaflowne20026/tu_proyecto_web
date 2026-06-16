from django.shortcuts import render, get_object_or_404
from .models import Servicio, Portada, InfoNosotros

def inicio(request):
    servicios = Servicio.objects.all().order_by('orden')
    portadas = Portada.objects.all()
    info = InfoNosotros.objects.first()
    return render(request, 'inicio.html', {'servicios': servicios, 'portadas': portadas, 'info': info})

def detalle_servicio(request, pk):
    servicio = get_object_or_404(Servicio, pk=pk)
    return render(request, 'detalle_servicio.html', {'servicio': servicio})

