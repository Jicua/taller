from django import forms
from .models import Cliente, Vehiculo, Atencion

class ClienteForm(forms.ModelForm):
	class Meta:
		model = Cliente
		fields = [
			'rut',
			'nombre',
			'telefono',
			'email'
		]

class VehiculoForm(forms.ModelForm):
	class Meta:
		model = Vehiculo
		fields = [
			'id_cliente',
			'patente',
			'marca',
			'modelo',
			'kilometraje'
		]

class AtencionForm(forms.ModelForm):
	class Meta:
		model = Atencion
		fields = [
			'id_vehiculo',
			'fecha_entrada',
			'fecha_salida'
		]