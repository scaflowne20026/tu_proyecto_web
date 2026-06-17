import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from servicios.models import Servicio

# Nombres EXACTOS de la BD (sin tildes, tal como aparecen en repr())
imagenes = {
    'Instalacion de aire acondicionados': 'servicios/aire.jpg',
    'instalacion de camaras de seguridad': 'servicios/camaras.jpg',
    'Instalaciones electricas': 'servicios/electricidad.jpg',
    'Pintado de Casas y Edificaciones': 'servicios/pintura.jpg',
    'instacion de porcelanato y ceramicos': 'servicios/porcelanato.jpg',
    'Instalaciones Sanitarias': 'servicios/sanitarias.jpg',
}

print("Asignando imagenes a servicios...\n")

for nombre, ruta in imagenes.items():
    try:
        servicio = Servicio.objects.get(nombre=nombre)
        servicio.imagen = ruta
        servicio.save()
        print(f"✅ {nombre} -> {ruta}")
    except Servicio.DoesNotExist:
        print(f"❌ No existe: {nombre}")

print("\n¡Listo!")
