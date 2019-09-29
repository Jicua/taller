from django import forms
from .models import Cliente, Vehiculo, Atencion, Detalle, Imagen

class ClienteForm(forms.ModelForm):
	class Meta:
		model = Cliente
		fields = [
			'rut',
			'nombre',
			'telefono',
			'email'
		]

class RawClienteForm(forms.Form):
	rut			= forms.CharField(max_length=10)
	nombre		= forms.CharField()
	telefono	= forms.CharField(label='Teléfono')
	email		= forms.CharField(required=False, label='E-mail')

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

class DetalleForm(forms.ModelForm):
	class Meta:
		model = Detalle
		fields = [
			'id_atencion',
			'descripcion'
		]

class ImagenForm(forms.ModelForm):
	class Meta:
		model = Imagen
		fields = [
			'id_detalle',
			'ubicacion',
			'descripcion'
		]