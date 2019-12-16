from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .forms import HoraForm
from .models import Hora
import datetime
from datetime import date
import locale
locale.setlocale(locale.LC_ALL,'es_CL.UTF-8')

# Create your views here.

def horas_home_view(request, *args, **kwargs):
	dia1 = date.today()
	if dia1.weekday() == 5: # hoy es sabado
		dia1 = dia1 + datetime.timedelta(days=2)
		dia2 = dia1 + datetime.timedelta(days=1)
		dia3 = dia2 + datetime.timedelta(days=1)
		dia4 = dia3 + datetime.timedelta(days=1)
		dia5 = dia4 + datetime.timedelta(days=1)

	elif dia1.weekday() == 6: # hoy es domingo
		dia1 = dia1 + datetime.timedelta(days=1)
		dia2 = dia1 + datetime.timedelta(days=1)
		dia3 = dia2 + datetime.timedelta(days=1)
		dia4 = dia3 + datetime.timedelta(days=1)
		dia5 = dia4 + datetime.timedelta(days=1)

	elif dia1.weekday() == 0: # hoy es lunes
		dia2 = dia1 + datetime.timedelta(days=1)
		dia3 = dia2 + datetime.timedelta(days=1)
		dia4 = dia3 + datetime.timedelta(days=1)
		dia5 = dia4 + datetime.timedelta(days=1)

	elif dia1.weekday() == 1: # hoy es martes
		dia2 = dia1 + datetime.timedelta(days=1)
		dia3 = dia2 + datetime.timedelta(days=1)
		dia4 = dia3 + datetime.timedelta(days=1)
		dia5 = dia4 + datetime.timedelta(days=3)

	elif dia1.weekday() == 2: # hoy es miercoles
		dia2 = dia1 + datetime.timedelta(days=1)
		dia3 = dia2 + datetime.timedelta(days=1)
		dia4 = dia3 + datetime.timedelta(days=3)
		dia5 = dia4 + datetime.timedelta(days=1)

	elif dia1.weekday() == 3: # hoy es jueves
		dia2 = dia1 + datetime.timedelta(days=1)
		dia3 = dia2 + datetime.timedelta(days=3)
		dia4 = dia3 + datetime.timedelta(days=1)
		dia5 = dia4 + datetime.timedelta(days=1)

	elif dia1.weekday() == 4: # hoy es viernes
		dia2 = dia1 + datetime.timedelta(days=3)
		dia3 = dia2 + datetime.timedelta(days=1)
		dia4 = dia3 + datetime.timedelta(days=1)
		dia5 = dia4 + datetime.timedelta(days=1)

	dia1nombre = dia1.strftime("%A %d")
	dia2nombre = dia2.strftime("%A %d")
	dia3nombre = dia3.strftime("%A %d")
	dia4nombre = dia4.strftime("%A %d")
	dia5nombre = dia5.strftime("%A %d")

	dia1str = dia1.strftime("%Y-%m-%d")
	dia2str = dia2.strftime("%Y-%m-%d")
	dia3str = dia3.strftime("%Y-%m-%d")
	dia4str = dia4.strftime("%Y-%m-%d")
	dia5str = dia5.strftime("%Y-%m-%d")

	bloques_tomados_dia1 = []
	bloques_tomados_dia2 = []
	bloques_tomados_dia3 = []
	bloques_tomados_dia4 = []
	bloques_tomados_dia5 = []

	now = datetime.datetime.now()
	horas_tomadas = Hora.objects.filter(anyo__gte=now.year).filter(mes__gte=now.month).filter(dia__gte=now.day)

	for hora_tomada in horas_tomadas:

		if hora_tomada.dia == dia1.day:
			if hora_tomada.bloque == 1:
				bloques_tomados_dia1.append(1)
			if hora_tomada.bloque == 2:
				bloques_tomados_dia1.append(2)
			if hora_tomada.bloque == 3:
				bloques_tomados_dia1.append(3)
			if hora_tomada.bloque == 4:
				bloques_tomados_dia1.append(4)

		if hora_tomada.dia == dia2.day:
			if hora_tomada.bloque == 1:
				bloques_tomados_dia2.append(1)
			if hora_tomada.bloque == 2:
				bloques_tomados_dia2.append(2)
			if hora_tomada.bloque == 3:
				bloques_tomados_dia2.append(3)
			if hora_tomada.bloque == 4:
				bloques_tomados_dia2.append(4)

		if hora_tomada.dia == dia3.day:
			if hora_tomada.bloque == 1:
				bloques_tomados_dia3.append(1)
			if hora_tomada.bloque == 2:
				bloques_tomados_dia3.append(2)
			if hora_tomada.bloque == 3:
				bloques_tomados_dia3.append(3)
			if hora_tomada.bloque == 4:
				bloques_tomados_dia3.append(4)

		if hora_tomada.dia == dia4.day:
			if hora_tomada.bloque == 1:
				bloques_tomados_dia4.append(1)
			if hora_tomada.bloque == 2:
				bloques_tomados_dia4.append(2)
			if hora_tomada.bloque == 3:
				bloques_tomados_dia4.append(3)
			if hora_tomada.bloque == 4:
				bloques_tomados_dia4.append(4)

		if hora_tomada.dia == dia5.day:
			if hora_tomada.bloque == 1:
				bloques_tomados_dia5.append(1)
			if hora_tomada.bloque == 2:
				bloques_tomados_dia5.append(2)
			if hora_tomada.bloque == 3:
				bloques_tomados_dia5.append(3)
			if hora_tomada.bloque == 4:
				bloques_tomados_dia5.append(4)
		
	context = {
		'dia1': dia1nombre,
		'dia2': dia2nombre,
		'dia3': dia3nombre,
		'dia4': dia4nombre,
		'dia5': dia5nombre,
		'dia1real': dia1str,
		'dia2real': dia2str,
		'dia3real': dia3str,
		'dia4real': dia4str,
		'dia5real': dia5str,
		'bloques_tomados_dia1': bloques_tomados_dia1,
		'bloques_tomados_dia2': bloques_tomados_dia2,
		'bloques_tomados_dia3': bloques_tomados_dia3,
		'bloques_tomados_dia4': bloques_tomados_dia4,
		'bloques_tomados_dia5': bloques_tomados_dia5
	}
	return render(request, "horas.html", context)

def reserva_view(request, *args, **kwargs):
	if request.method == "POST":
		fecha = request.POST.get("fecha")
		nombre = request.POST.get("nombre")
		telefono = request.POST.get("telefono")
		email = request.POST.get("email")
		hora = request.POST.get("hora")
		diaSemana = request.POST.get("diaSemana")
		context = {
			'post': True,
			'nombre': nombre,
			'diaSemana': diaSemana,
			'hora': hora
		}
		form = HoraForm(request.POST or None)
		if form.is_valid():
			form.save()
			form = HoraForm()
			return render(request, "reserva.html", context)
		else:
			context = {
			'error': True
			}
			print (form.errors)
		return render(request, "reserva.html", context)
	else:
		diaSemana = request.GET['dia']
		diaSemana = diaSemana.title()
		bloque = request.GET['bloque']
		fecha = request.GET['fecha']
		anyo, mes, dia = fecha.split('-')
		if bloque == "1":
			hora = "9:00"
		elif bloque == "2":
			hora = "11:00"
		elif bloque == "3":
			hora = "15:00"
		else:
			hora = "17:00"
		form = HoraForm(request.POST or None)
		context = {
			'form': form,
			'fecha': fecha,
			'dia': dia,
			'bloque': bloque,
			'mes': mes,
			'anyo': anyo,
			'diaSemana': diaSemana,
			'hora': hora,
			'error': False
		}

		return render(request, "reserva.html", context)

@login_required
def admin_view(request, *args, **kwargs):
	locale.setlocale(locale.LC_ALL,'es_ES.UTF-8')
	now = datetime.datetime.now()
	horas = Hora.objects.filter(fecha__gte=now).order_by('fecha', 'bloque')
	listado_horas = []
	for hora in horas:
		listado_horas.append(hora)
	context = {
		'horas': horas
	}
	return render(request, "horas_admin.html", context)

def admin_view_todas(request, *args, **kwargs):
	horas = Hora.objects.all().order_by('fecha', 'bloque')
	listado_horas = []
	for hora in horas:
		listado_horas.append(hora)
	context = {
		'horas': horas
	}
	return render(request, "horas_admin_todas.html", context)