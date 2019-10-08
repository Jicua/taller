from django.db import models
from django.urls import reverse

# Create your models here.

class Cliente(models.Model):
	rut			= models.CharField(max_length = 10)
	nombre		= models.CharField(max_length = 100)
	telefono	= models.CharField(max_length = 12)
	email		= models.CharField(max_length = 100, blank = True)

	def get_absolute_url(self):
		return reverse("fichas:cliente-detail", kwargs={"id": self.id})
	
	def __str__(self):
		return self.nombre

class Vehiculo(models.Model):
	id_cliente	= models.ForeignKey('Cliente', blank = True, null = True, on_delete = models.SET_NULL, verbose_name='Dueño')
	patente		= models.CharField(max_length = 6)
	vin 		= models.CharField(max_length = 20, blank = True, null = True)
	marca		= models.CharField(max_length = 40)
	modelo		= models.CharField(max_length = 40)
	kilometraje	= models.PositiveIntegerField()
	anyo		= models.PositiveIntegerField(null = True)

	def get_absolute_url(self):
		return reverse("fichas:vehiculo-detail", kwargs={"id": self.id})

	def __str__(self):
		return  self.marca + ' ' + self.modelo
	
class Atencion(models.Model):
	id_vehiculo		= models.ForeignKey('Vehiculo', on_delete=models.CASCADE, verbose_name='Vehículo')
	fecha_entrada	= models.DateTimeField()
	fecha_salida	= models.DateTimeField(blank=True)
	observaciones	= models.CharField(blank=True, max_length=500)

	def get_absolute_url(self):
		return reverse("fichas:atencion-detail", kwargs={"id": self.id_vehiculo, "at": self.id})

	#def get_relative_url(self):
	#	return reverse("fichas:vehiculo-atencion-detail", kwargs={"at": self.id})
	
class Detalle(models.Model):
	id_atencion	= models.ForeignKey('Atencion', on_delete=models.CASCADE, verbose_name='Atención')
	descripcion	= models.TextField(blank=True)
	
class Imagen(models.Model):
	id_detalle	= models.ForeignKey('Detalle', on_delete=models.CASCADE, verbose_name='Detalle')
	ubicacion	= models.CharField(max_length=255) # file path relativo
	descripcion	= models.TextField(blank=True)
