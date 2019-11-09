import re
from django import forms
from .models import Cliente, Vehiculo, Atencion, Detalle, Imagen

class ClienteForm(forms.ModelForm):
	rut			= forms.CharField(max_length=10, widget=forms.TextInput(attrs={"placeholder": "Ingrese rut"}))
	nombre		= forms.CharField(max_length = 100)
	telefono	= forms.CharField(label='Teléfono', max_length = 12, initial="+56")
	email		= forms.CharField(required=False, label='E-mail', max_length = 100)

	class Meta:
		model = Cliente
		fields = [
			'rut',
			'nombre',
			'telefono',
			'email'
		]

	def clean_rut(self, *args, **kwargs):
		rut = self.cleaned_data.get("rut")
		rut = rut.upper()
		valid = re.compile('\d{7,8}-[\dK]')
		if valid.match(rut) == None:
			raise forms.ValidationError("Rut inválido")
		else:
			return rut

	def clean_nombre(self, *args, **kwargs):
		nombre = self.cleaned_data.get("nombre")
		nombre = nombre.title()
		valid = re.compile('[A-Z][a-zA-Z][^#&<>\"~;$^%{}?]{1,40}$')
		if valid.match(nombre) == None:
			raise forms.ValidationError("Nombre inválido")
		else:
			return nombre

	def clean_telefono(self, *args, **kwargs):
		telefono = self.cleaned_data.get("telefono")
		valid = re.compile('^\+\d{8,11}|\d{8,11}')
		if valid.match(telefono) == None:
			raise forms.ValidationError("Teléfono inválido")
		else:
			return telefono


	def clean_email(self, *args, **kwargs):
		email = self.cleaned_data.get("email")
		valid = re.compile('^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')
		if valid.match(email) == None:
			raise forms.ValidationError("E-mail inválido")
		else:
			return email



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

	def clean_patente(self, *args, **kwargs):
		patente = self.cleaned_data.get("patente")
		patente = patente.upper()
		valid = re.compile('[A-z]{4}\d{2}|[A-z]{2}\d{4}')
		if valid.match(patente) == None:
			raise forms.ValidationError("Patente inválida")
		else:
			return patente

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
	id_vehiculo		= forms.ModelChoiceField(queryset=Vehiculo.objects.all())
	fecha_entrada	= forms.DateField()
	fecha_salida	= forms.DateField(required=False)
	hora_entrada	= forms.TimeField(required=False)
	hora_salida		= forms.TimeField(required=False)
	observaciones	= forms.CharField()
	widgets = {'id_vehiculo': forms.HiddenInput()}
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
	descripcion = forms.CharField(label='aaa', widget=forms.Textarea(attrs={"placeholder": "Ingrese descripción"}))

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