from django.contrib import admin
from .models import Servicio, Portada, InfoNosotros

class ServicioAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'orden')
    ordering = ['orden']

admin.site.register(Servicio, ServicioAdmin)
admin.site.register(Portada)
admin.site.register(InfoNosotros)
