from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required

from django.views.generic import (
	ListView,
	DetailView
	)

from .models import Cliente, Vehiculo, Atencion, Detalle, Imagen

from .forms import ClienteForm, VehiculoForm, AtencionForm, DetalleForm, ImagenForm
from .forms import RawClienteForm, RawVehiculoForm, RawAtencionForm

# Create your views here.

@login_required
def fichas_home_view(request, *args, **kwargs):
	return render(request, "fichas.html", {})

##########################
######## CLIENTE #########
##########################

@login_required
@staff_member_required
def cliente_create_view(request):
	my_form = RawClienteForm(request.POST or None)
	if my_form.is_valid():
		Cliente.objects.create(**my_form.cleaned_data)
		my_form = RawClienteForm()
	context = {
		'form': my_form
	}
	return render(request, "clientes/cliente_create.html", context)

@login_required
@staff_member_required
def cliente_update_view(request, id=id):
	obj = get_object_or_404(Cliente, id=id)
	form = ClienteForm(request.POST or None, instance=obj)
	if form.is_valid():
		form.save()
	context = {
		'form': form
	}
	return render(request, "clientes/cliente_create.html", context)

@login_required
def cliente_list_view(request):
	queryset = Cliente.objects.all()
	context = {
		"object_list": queryset
	}
	return render(request, "clientes/cliente_list.html", context)

@login_required
def cliente_detail_view(request, id):
	obj = get_object_or_404(Cliente, id=id)
	vehiculos = Vehiculo.objects.all().filter(id_cliente=id)
	context = {
		"object": obj,
		"vehiculos_list": vehiculos
	}
	return render(request, "clientes/cliente_detail.html", context)

@login_required
@staff_member_required
def cliente_delete_view(request, id):
	obj = get_object_or_404(Cliente, id=id)
	if request.method == "POST":
		obj.delete()
		return redirect('../../')
	context = {
		"object": obj
	}
	return render(request, "clientes/cliente_delete.html", context)

class ClienteListView(ListView):
	template_name = 'clientes/cliente_list.html'
	queryset = Cliente.objects.all()

class ClienteDetailView(DetailView):
	template_name = 'clientes/cliente_detail.html'
	queryset = Cliente.objects.all()

	def get_object(self):
		id_ = self.kwargs.get("id")
		return get_object_or_404(Cliente, id=id_)

##########################
######## VEHICULO ########
##########################

@login_required
@staff_member_required
def vehiculo_create_view(request, cliente = 0):
	form = RawVehiculoForm(request.POST or None)
	if form.is_valid():
		Vehiculo.objects.create(**form.cleaned_data)
		form = RawVehiculoForm()
	clientes = Cliente.objects.all().order_by('nombre')
	if cliente != 0:
		duenyo = get_object_or_404(Cliente, id=cliente)
		context = {
			'form': form,
			'clientes': clientes,
			'duenyo': duenyo
		}
	else:
		context = {
			'form': form,
			'clientes': clientes,
		}
	return render(request, "vehiculos/vehiculo_create.html", context)

@login_required
@staff_member_required
def vehiculo_update_view(request, id=id):
	obj = get_object_or_404(Vehiculo, id=id)
	form = VehiculoForm(request.POST or None, instance=obj)
	if form.is_valid():
		form.save()
	context = {
		'form': form
	}
	return render(request, "vehiculos/vehiculo_create.html", context)

@login_required
def vehiculo_list_view(request):
	queryset = Vehiculo.objects.all()
	context = {
		"object_list": queryset
	}
	return render(request, "vehiculos/vehiculo_list.html", context)

@login_required
def vehiculo_detail_view(request, id):
	obj = get_object_or_404(Vehiculo, id=id)
	atenciones = Atencion.objects.all().filter(id_vehiculo=id)
	context = {
		"object": obj,
		"atenciones_list": atenciones
	}
	return render(request, "vehiculos/vehiculo_detail.html", context)

@login_required
@staff_member_required
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

@login_required
@staff_member_required
def atencion_create_view(request, id):
	form = RawAtencionForm(request.POST or None)
	if form.is_valid():
		Atencion.objects.create(**form.cleaned_data)
		form = RawAtencionForm()
	auto = get_object_or_404(Vehiculo, id=id)
	context = {
		'form': form,
		'vehiculo': auto
	}
	print(request.POST)
	return render(request, "atenciones/atencion_create.html", context)

@login_required
@staff_member_required
def atencion_update_view(request, id, at):
	obj = get_object_or_404(Atencion, id=at)
	form = AtencionForm(request.POST or None, instance=obj)
	if form.is_valid():
		form.save()
	context = {
		'form': form
	}
	return render(request, "atenciones/atencion_create.html", context)

@login_required
def atencion_list_view(request):
 	queryset = Atencion.objects.all()
 	context = {
 		"object_list": queryset
 	}
 	return render(request, "atenciones/atencion_list.html", context)

@login_required
def atencion_detail_view(request, id, at):
	obj = get_object_or_404(Atencion, id=at)
	detalles = Detalle.objects.all().filter(id_atencion=at)
	context = {
		"object": obj,
		"detalles_list": detalles
	}
	return render(request, "atenciones/atencion_detail.html", context)

@login_required
@staff_member_required
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

@login_required
@staff_member_required
def detalle_create_view(request, id, at):
	form = DetalleForm(request.POST or None)
	if form.is_valid():
		form.save()
		form = DetalleForm()
	context = {
		'form': form
	}
	return render(request, "detalles/detalle_create.html", context)

@login_required
def detalle_detail_view(request, id, at, de):
	obj = get_object_or_404(Detalle, id=de)
	context = {
		"object": obj,
	}
	return render(request, "detalles/detalle_detail.html", context)

@login_required
@staff_member_required
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