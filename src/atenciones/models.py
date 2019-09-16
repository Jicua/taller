from django.db import models

class Atencion(models.Model):
	id_vehiculo	= models.ForeignKey('vehiculos.Vehiculo'),
	fecha_entrada	= models.DateTimeField(),
	fecha_salida	= models.DateTimeField(blank = True)
