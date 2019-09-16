from django.db import models

class Detalle(models.Model):
	id_atencion	= models.ForeignKey('atenciones.Atencion'),
	descripcion	= models.TextField(blank = True),
