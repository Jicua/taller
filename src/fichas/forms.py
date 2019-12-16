import re
from django import forms
from .models import Cliente, Vehiculo, Atencion, Detalle

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
		email = email.lower()
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
			'anyo',
			'imagen'
		]

	def clean_patente(self, *args, **kwargs):
		patente = self.cleaned_data.get("patente")
		patente = patente.upper()
		valid = re.compile('[A-z]{4}\d{2}|[A-z]{2}\d{4}')
		if valid.match(patente) == None:
			raise forms.ValidationError("Patente inválida")
		else:
			return patente

	def clean_vin(self, *args, **kwargs):
		vin = self.cleaned_data.get("vin")
		valid = re.compile('\d{20}')
		if valid.match(vin) == None:
			raise forms.ValidationError("Vin inválido")
		else:
			return vin

	def clean_tipo(self, *args, **kwargs):
		tipo = self.cleaned_data.get("tipo")
		validos = ("Sedán", "Hatchback", "Station Wagon", "SUV", "Camioneta", "Furgón")
		if tipo in validos:
			return tipo
		else:
			raise forms.ValidationError("Tipo inválido")

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
			'estado',
			'fecha_entrada',
			'fecha_salida',
			'hora_entrada',
			'hora_salida',
			'observaciones'
		]
		
	def clean_observaciones(self, *args, **kwargs):
		observaciones = self.cleaned_data.get("observaciones")
		observaciones = observaciones.capitalize()
		return observaciones

class RawAtencionForm(forms.Form):
	id_vehiculo		= forms.ModelChoiceField(queryset=Vehiculo.objects.all())
	fecha_entrada	= forms.DateField()
	fecha_salida	= forms.DateField(required=False)
	hora_entrada	= forms.TimeField(required=False)
	hora_salida		= forms.TimeField(required=False)
	observaciones	= forms.CharField()

class DetalleForm(forms.ModelForm):
	descripcion = forms.CharField(widget=forms.Textarea(attrs={"placeholder": "Ingrese descripción"}))
	repuesto 	= forms.CharField(required=False, widget=forms.TextInput(attrs={"placeholder": "Ingrese repuesto"}))

	class Meta:
		model = Detalle
		fields = [
			'id_atencion',
			'descripcion',
			'image',
			'repuesto',
			'valor_repuesto'
		]

	def clean_descripcion(self, *args, **kwargs):
		descripcion = self.cleaned_data.get("descripcion")
		descripcion = descripcion.capitalize()
		return descripcion

	def clean_repuesto(self, *args, **kwargs):
		repuesto = self.cleaned_data.get("repuesto")
		repuesto = repuesto.capitalize()
		return repuesto