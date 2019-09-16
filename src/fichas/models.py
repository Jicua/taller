from django.db import models

class Cliente(models.Model):
	rut		= models.CharField(max_length = 10),
	nombre		= models.CharField(max_length = 100),
	telefono	= models.CharField(max_length = 12),
	email		= models.CharField(max_length = 100, blank = True)
	
class Vehiculo(models.Model):
	id_cliente	= models.ForeignKey(Cliente),
	patente		= models.CharField(max_length = 6),
	marca		= models.CharField(max_length = 40),
	modelo		= models.CharField(max_length = 40),
	kilometraje	= models.PositiveIntegerField()
	
class Atencion(models.Model):
	id_vehiculo	= models.ForeignKey(Vehiculo),
	fecha_entrada	= models.DateTimeField(),
	fecha_salida	= models.DateTimeField(blank = True)
	
class Detalle(models.Model):
	id_atencion	= models.ForeignKey(Atencion),
	descripcion	= models.TextField(blank = True),
	
class Imagen(models.Model):
	id_detalle	= models.ForeignKey(Detalle),
	ubicacion	= models.CharField(max_length = 255), # file path relativo
	descripcion	= models.TextField(blank = True)
