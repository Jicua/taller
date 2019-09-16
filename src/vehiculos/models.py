from django.db import models

class Vehiculo(models.Model):
	id_cliente	= models.ForeignKey('clientes.Cliente'),
	patente		= models.CharField(max_length = 6),
	marca		= models.CharField(max_length = 40),
	modelo		= models.CharField(max_length = 40),
	kilometraje	= models.PositiveIntegerField()
