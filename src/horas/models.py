from django.db import models

# Create your models here.

class Hora(models.Model):
	fecha	= models.DateField(null=True)
	dia		= models.PositiveIntegerField()
	bloque  = models.PositiveIntegerField()
	mes 	= models.PositiveIntegerField()
	anyo	= models.PositiveIntegerField()
	nombre	= models.CharField(max_length = 100)
	telefono	= models.CharField(max_length = 12)
	email		= models.CharField(max_length = 100, blank = True)
	observaciones	= models.CharField(max_length=512, blank = True)