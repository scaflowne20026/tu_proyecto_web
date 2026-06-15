from django.contrib import admin
from .models import Servicio

class ServicioAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'orden', 'activo')
    fields = ('nombre', 'descripcion', 'lista_servicios', 'por_que_elegirnos', 'imagen', 'activo', 'orden')

admin.site.register(Servicio, ServicioAdmin)
