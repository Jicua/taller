from django.db import models

class Cliente(models.Model):
	rut			= models.CharField(max_length = 10),
	nombre		= models.CharField(max_length = 100),
	telefono	= models.CharField(max_length = 12),
	email		= models.CharField(max_length = 100, blank = True)
