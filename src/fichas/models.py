import random
from django.db import models
from django.db.models import Q
from django.urls import reverse

# Create your models here.

class ClienteQuerySet(models.QuerySet):
	def search(self, query):
		lookup = (
				Q(nombre__icontains=query) | 
				Q(rut__icontains=query)
				)
		return self.filter(lookup)

class ClienteManager(models.Manager):
	def get_queryset(self):
		return ClienteQuerySet(self.model, using=self._db)

	def search(self, query = None):
		if query == None:
			return self.get_queryset().none()
		return self.get_queryset().search(query)

class Cliente(models.Model):
	rut			= models.CharField(max_length = 10)
	nombre		= models.CharField(max_length = 100)
	telefono	= models.CharField(max_length = 12)
	email		= models.CharField(max_length = 100, blank = True)

	objects		= ClienteManager()

	def get_absolute_url(self):
		return reverse("fichas:cliente-detail", kwargs={"id": self.id})
	
	def __str__(self):
		return self.nombre

class VehiculoQuerySet(models.QuerySet):
	def search(self, query):
		lookup = (
				Q(marca__icontains=query) | 
				Q(modelo__icontains=query) |
				Q(tipo__icontains=query) |
				Q(patente__icontains=query)
				)
		return self.filter(lookup)

class VehiculoManager(models.Manager):
	def get_queryset(self):
		return VehiculoQuerySet(self.model, using=self._db)

	def search(self, query = None):
		if query == None:
			return self.get_queryset().none()
		return self.get_queryset().search(query)

class Vehiculo(models.Model):
	id_cliente	= models.ForeignKey('Cliente', blank = True, null = True, on_delete = models.SET_NULL, verbose_name='Dueño')
	patente		= models.CharField(max_length = 6)
	vin 		= models.CharField(max_length = 20, blank = True, null = True)
	tipo		= models.CharField(max_length = 40, default="Sedán")
	marca		= models.CharField(max_length = 40)
	modelo		= models.CharField(max_length = 40)
	kilometraje	= models.PositiveIntegerField()
	anyo		= models.PositiveIntegerField(null = True)

	objects		= VehiculoManager()

	def get_absolute_url(self):
		return reverse("fichas:vehiculo-detail", kwargs={"id": self.id})

	def get_url(id):
		return reverse("fichas:vehiculo-detail", kwargs={"id": id})

	#def __str__(self):
	#	return  self.marca + ' ' + self.modelo

def create_pin():
	return random.randint(999, 9999)

class AtencionQuerySet(models.QuerySet):
	def search(self, query):
		lookup = (
				Q(observaciones__icontains=query) |
				Q(id_vehiculo__marca__icontains=query) |
				Q(id_vehiculo__modelo__icontains=query) |
				Q(id_vehiculo__id_cliente__nombre__icontains=query)
				)
		return self.filter(lookup)

class AtencionManager(models.Manager):
	def get_queryset(self):
		return AtencionQuerySet(self.model, using=self._db)

	def search(self, query = None):
		if query == None:
			return self.get_queryset().none()
		return self.get_queryset().search(query)

class Atencion(models.Model):
	id_vehiculo		= models.ForeignKey('Vehiculo', on_delete=models.CASCADE, verbose_name='Vehículo')
	pin				= models.CharField(max_length=4, default=create_pin)
	estado			= models.BooleanField(default=True)
	fecha_entrada	= models.DateField()
	fecha_salida	= models.DateField(blank=True, null=True)
	hora_entrada	= models.TimeField(blank=True, null=True)
	hora_salida		= models.TimeField(blank=True, null=True)
	observaciones	= models.CharField(max_length=500)

	objects			= AtencionManager()

	def get_absolute_url(self):
		return reverse("fichas:atencion-detail", kwargs={"id": self.id_vehiculo, "at": self.id})

	#def get_relative_url(self):
	#	return reverse("fichas:vehiculo-atencion-detail", kwargs={"at": self.id})
	
class Detalle(models.Model):
	id_atencion	= models.ForeignKey('Atencion', on_delete=models.CASCADE, verbose_name='Atención')
	descripcion	= models.TextField(blank=True)
	image 		= models.ImageField(upload_to='image/', blank=True, null=True)

class Imagen(models.Model):
	id_detalle	= models.ForeignKey('Detalle', on_delete=models.CASCADE, verbose_name='Detalle')
	ubicacion	= models.CharField(max_length=255, blank=True, null=True) # file path relativo
	descripcion	= models.TextField(blank=True)
	imagen 		= models.ImageField(upload_to='image/', blank=True, null=True)

class SearchQuery(models.Model):
	query = models.CharField(max_length=128)