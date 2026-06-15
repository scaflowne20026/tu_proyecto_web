from django.db import models

class Servicio(models.Model):
    nombre = models.CharField(max_length=200, verbose_name="Nombre del servicio")
    descripcion = models.TextField(verbose_name="1. Descripción completa")
    lista_servicios = models.TextField(blank=True, verbose_name="2. Nuestros Servicios")
    por_que_elegirnos = models.TextField(blank=True, verbose_name="3. ¿Por qué elegirnos?")
    imagen = models.ImageField(upload_to='servicios/')
    activo = models.BooleanField(default=True)
    orden = models.PositiveIntegerField(default=1)

    def __str__(self):
        return self.nombre
