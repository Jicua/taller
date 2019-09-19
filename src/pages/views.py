from django.shortcuts import render

# Create your views here.

def home_view(request, *args, **kwargs):
	return render(request, "home.html", {})

def contact_view(request, *args, **kwargs):
	my_context = {
		"nombre": "Ricardo Lüer",
		"telefono": "123456789",
		"direccion": "Vial 365",
		"lista": [123, 456, 789]
	}
	return render(request, "contact.html", my_context)