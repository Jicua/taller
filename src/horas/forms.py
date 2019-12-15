import re
from django import forms
from .models import Hora

class HoraForm(forms.ModelForm):
	fecha		= forms.DateField(widget = forms.HiddenInput())
	dia			= forms.IntegerField(widget = forms.HiddenInput())
	bloque  	= forms.IntegerField(widget = forms.HiddenInput())
	mes 		= forms.IntegerField(widget = forms.HiddenInput())
	anyo		= forms.IntegerField(widget = forms.HiddenInput())
	nombre		= forms.CharField(max_length = 100)
	telefono	= forms.CharField(max_length = 12)
	email		= forms.CharField(max_length = 100, required = False)
	observaciones	= forms.CharField(max_length = 512, required = False, widget=forms.Textarea(attrs={"placeholder": "Ingrese un mensaje para el mecánico", "rows": 4}))

	class Meta:
		model = Hora
		fields = [
			'fecha',
			'dia',
			'bloque',
			'mes',
			'anyo',
			'nombre',
			'telefono',
			'email',
			'observaciones'
		]