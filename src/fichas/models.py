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
	id_cliente	= models.ForeignKey('Cliente', null = True, on_delete = models.SET_NULL, verbose_name='Dueño')
	patente		= models.CharField(max_length = 6)
	marca		= models.CharField(max_length = 40)
	modelo		= models.CharField(max_length = 40)
	kilometraje	= models.PositiveIntegerField()

	def get_absolute_url(self):
		return reverse("fichas:vehiculo-detail", kwargs={"id": self.id})

	def __str__(self):
		return  self.marca + ' ' + self.modelo
	
class Atencion(models.Model):
	id_vehiculo		= models.ForeignKey('Vehiculo', on_delete=models.CASCADE, verbose_name='Vehículo')
	fecha_entrada	= models.DateTimeField()
	fecha_salida	= models.DateTimeField(blank = True)

	def get_absolute_url(self):
		return reverse("fichas:atencion-detail", kwargs={"id": self.id})
	
class Detalle(models.Model):
	id_atencion	= models.ForeignKey('Atencion', on_delete=models.CASCADE)
	descripcion	= models.TextField(blank = True)
	
class Imagen(models.Model):
	id_detalle	= models.ForeignKey('Detalle', on_delete=models.CASCADE)
	ubicacion	= models.CharField(max_length = 255) # file path relativo
	descripcion	= models.TextField(blank = True)
