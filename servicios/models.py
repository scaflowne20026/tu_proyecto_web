from django.db import models

class Servicio(models.Model):
    nombre = models.CharField(max_length=120)
    descripcion = models.TextField(blank=True)
    imagen = models.ImageField(upload_to='servicios/', blank=True, null=True)
    titulo_columna_izq = models.CharField(max_length=120, blank=True)
    texto_columna_izq = models.TextField(blank=True)
    titulo_columna_der = models.CharField(max_length=120, blank=True)
    texto_columna_der = models.TextField(blank=True)
    orden = models.PositiveIntegerField(default=1, help_text="1 = primero, 2 = segundo...")

    def __str__(self):
        return self.nombre


class Portada(models.Model):
    titulo = models.CharField(max_length=120, blank=True)
    imagen = models.ImageField(upload_to='portadas/')

    def __str__(self):
        return self.titulo or "Portada"


class InfoNosotros(models.Model):
    titulo_principal = models.CharField(max_length=120)
    subtitulo = models.CharField(max_length=200, blank=True)
    descripcion_1 = models.TextField()
    descripcion_2 = models.TextField(blank=True)
    pie_lista = models.TextField(blank=True, help_text="Una línea por ítem")
    imagen_equipo = models.ImageField(upload_to='nosotros/', blank=True, null=True)

    def __str__(self):
        return self.titulo_principal
