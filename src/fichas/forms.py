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
	nombre		= forms.CharField(max_length = 100)
	telefono	= forms.CharField(label='Teléfono', max_length = 12)
	email		= forms.CharField(required=False, label='E-mail', max_length = 100)

class VehiculoForm(forms.ModelForm):
	class Meta:
		model = Vehiculo
		fields = [
			'id_cliente',
			'patente',
			'vin',
			'tipo',
			'marca',
			'modelo',
			'kilometraje',
			'anyo'
		]

class RawVehiculoForm(forms.Form):
	#self.fields['id_cliente'].queryset	= Cliente.objects.filter(cliente=self.id_cliente)
	id_cliente	= forms.ModelChoiceField(queryset=Cliente.objects.all(), empty_label="(Ninguno)")
	patente		= forms.CharField(max_length=6)
	vin			= forms.CharField(max_length=20)
	tipo		= forms.CharField(max_length=40)
	marca		= forms.CharField(max_length = 40)
	modelo 		= forms.CharField(max_length = 40)
	kilometraje	= forms.IntegerField()
	anyo		= forms.IntegerField()

class AtencionForm(forms.ModelForm):
	class Meta:
		model = Atencion
		fields = [
			'id_vehiculo',
			'fecha_entrada',
			'fecha_salida',
			'hora_entrada',
			'hora_salida',
			'observaciones'
		]

class RawAtencionForm(forms.Form):
	id_vehiculo		= forms.ModelChoiceField(queryset=Vehiculo.objects.all())
	fecha_entrada	= forms.DateField()
	fecha_salida	= forms.DateField(required=False)
	hora_entrada	= forms.TimeField(required=False)
	hora_salida		= forms.TimeField(required=False)
	observaciones	= forms.CharField()

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