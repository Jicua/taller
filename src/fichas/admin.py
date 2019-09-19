from django.contrib import admin

# Register your models here.

from .models import Cliente, Vehiculo, Atencion, Detalle, Imagen

admin.site.register(Cliente)
admin.site.register(Vehiculo)
admin.site.register(Atencion)
admin.site.register(Detalle)
admin.site.register(Imagen)
