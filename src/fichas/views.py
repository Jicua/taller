from django.shortcuts import render, get_object_or_404, redirect

from .models import Cliente, Vehiculo, Atencion, Detalle, Imagen

from .forms import ClienteForm, VehiculoForm, AtencionForm, DetalleForm, ImagenForm
from .forms import RawClienteForm

# Create your views here.

def fichas_home_view(request, *args, **kwargs):
	return render(request, "fichas.html", {})

##########################
######## CLIENTE #########
##########################

def cliente_create_view(request):
	my_form = RawClienteForm(request.POST or None)
	if my_form.is_valid():
		Cliente.objects.create(**my_form.cleaned_data)
		my_form = RawClienteForm()
	context = {
		'form': my_form
	}
	return render(request, "clientes/cliente_create.html", context)

def cliente_update_view(request, id=id):
	obj = get_object_or_404(Cliente, id=id)
	form = ClienteForm(request.POST or None, instance=obj)
	if form.is_valid():
		form.save()
	context = {
		'form': form
	}
	return render(request, "clientes/cliente_create.html", context)

def cliente_list_view(request):
	queryset = Cliente.objects.all()
	context = {
		"object_list": queryset
	}
	return render(request, "clientes/cliente_list.html", context)

def cliente_detail_view(request, id):
	obj = get_object_or_404(Cliente, id=id)
	vehiculos = Vehiculo.objects.all().filter(id_cliente=id)
	context = {
		"object": obj,
		"vehiculos_list": vehiculos
	}
	return render(request, "clientes/cliente_detail.html", context)

def cliente_delete_view(request, id):
	obj = get_object_or_404(Cliente, id=id)
	if request.method == "POST":
		obj.delete()
		return redirect('../../')
	context = {
		"object": obj
	}
	return render(request, "clientes/cliente_delete.html", context)

##########################
######## VEHICULO ########
##########################

def vehiculo_create_view(request, cliente = 0):
	form = VehiculoForm(request.POST or None)
	if form.is_valid():
		form.save()
		form = VehiculoForm()
	clientes = Cliente.objects.all().order_by('nombre')
	context = {
		'form': form,
		'clientes': clientes
	}
	return render(request, "vehiculos/vehiculo_create.html", context)

def vehiculo_update_view(request, id=id):
	obj = get_object_or_404(Vehiculo, id=id)
	form = VehiculoForm(request.POST or None, instance=obj)
	if form.is_valid():
		form.save()
	context = {
		'form': form
	}
	return render(request, "vehiculos/vehiculo_create.html", context)

def vehiculo_list_view(request):
	queryset = Vehiculo.objects.all()
	context = {
		"object_list": queryset
	}
	return render(request, "vehiculos/vehiculo_list.html", context)

def vehiculo_detail_view(request, id):
	obj = get_object_or_404(Vehiculo, id=id)
	atenciones = Atencion.objects.all().filter(id_vehiculo=id)
	context = {
		"object": obj,
		"atenciones_list": atenciones
	}
	return render(request, "vehiculos/vehiculo_detail.html", context)

def vehiculo_delete_view(request, id):
	obj = get_object_or_404(Vehiculo, id=id)
	if request.method == "POST":
		obj.delete()
		return redirect('../../')
	context = {
		"object": obj
	}
	return render(request, "vehiculos/vehiculo_delete.html", context)

##########################
######## ATENCIÓN ########
##########################

def atencion_create_view(request, id):
	form = AtencionForm(request.POST or None)
	if form.is_valid():
		form.save()
		form = AtencionForm()
	vehiculo = id
	context = {
		'form': form,
		'vehiculo': vehiculo
	}
	return render(request, "atenciones/atencion_create.html", context)

def atencion_update_view(request, id, at):
	obj = get_object_or_404(Atencion, id=at)
	form = AtencionForm(request.POST or None, instance=obj)
	if form.is_valid():
		form.save()
	context = {
		'form': form
	}
	return render(request, "atenciones/atencion_create.html", context)

def atencion_list_view(request):
 	queryset = Atencion.objects.all()
 	context = {
 		"object_list": queryset
 	}
 	return render(request, "atenciones/atencion_list.html", context)

def atencion_detail_view(request, id, at):
	obj = get_object_or_404(Atencion, id=at)
	detalles = Detalle.objects.all().filter(id_atencion=at)
	context = {
		"object": obj,
		"detalles_list": detalles
	}
	return render(request, "atenciones/atencion_detail.html", context)

def atencion_delete_view(request, id, at):
	obj = get_object_or_404(Atencion, id=at)
	if request.method == "POST":
		obj.delete()
		return redirect('../../../')
	context = {
		"object": obj
	}
	return render(request, "atenciones/atencion_delete.html", context)

##########################
######## DETALLE #########
##########################

def detalle_create_view(request, id, at):
	form = DetalleForm(request.POST or None)
	if form.is_valid():
		form.save()
		form = DetalleForm()
	context = {
		'form': form
	}
	return render(request, "detalles/detalle_create.html", context)

def detalle_detail_view(request, id, at, de):
	obj = get_object_or_404(Detalle, id=de)
	context = {
		"object": obj,
	}
	return render(request, "detalles/detalle_detail.html", context)

def detalle_delete_view(request, id, at, de):
	obj = get_object_or_404(Detalle, id=de)
	if request.method == "POST":
		obj.delete()
		return redirect('../../../')
	context = {
		"object": obj
	}
	return render(request, "detalles/detalle_delete.html", context)

##########################
######## IMAGEN ##########
##########################