from django.urls import path

from django.contrib import admin
from django.urls import path, include

from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from .views import (
	fichas_home_view,

	cliente_list_view,
	cliente_create_view,
	cliente_detail_view,
	cliente_update_view,
	cliente_delete_view,

	ClienteListView,
	ClienteDetailView,

	vehiculo_list_view,
	vehiculo_create_view,
	vehiculo_detail_view,
	vehiculo_update_view,
	vehiculo_delete_view,

	atencion_list_view,
	atencion_create_view,
	atencion_detail_view,
	atencion_update_view,
	atencion_delete_view,

	detalle_create_view,
	detalle_detail_view,
	detalle_delete_view
	)

app_name = 'fichas'
urlpatterns = [
	path('', fichas_home_view, name='fichas'),

	######## CLIENTES #######

	path('clientes/', cliente_list_view, name='cliente-list'),
	path('clientes/crear/', cliente_create_view, name='cliente-create'),
	path('clientes/<int:id>/', cliente_detail_view, name='cliente-detail'),
	path('clientes/<int:id>/editar/', cliente_update_view, name='cliente-update'),
	path('clientes/<int:id>/eliminar/', cliente_delete_view, name='cliente-delete'),

	path('clientes2/', ClienteListView.as_view(), name="cliente-list2"),
	path('clientes2/<int:id>/', ClienteDetailView.as_view(), name="cliente-detail2"),

	######## VEHICULOS #######

	path('vehiculos/', vehiculo_list_view, name='vehiculo-list'),
	path('vehiculos/crear/', vehiculo_create_view, name='vehiculo-create'),
	path('vehiculos/crear/<int:cliente>', vehiculo_create_view, name='vehiculo-create'),
	path('vehiculos/<int:id>/', vehiculo_detail_view, name='vehiculo-detail'),
	path('vehiculos/<int:id>/editar/', vehiculo_update_view, name='vehiculo-update'),
	path('vehiculos/<int:id>/eliminar/', vehiculo_delete_view, name='vehiculo-delete'),

	####### ATENCIONES #######

	path('atenciones/', atencion_list_view, name ='atencion-list-view'),

	######## VEHICULOS/ATENCIONES #######

	path('vehiculos/<int:id>/atenciones/crear/', atencion_create_view, name='atencion-create'),
	path('vehiculos/<int:id>/atenciones/<int:at>/', atencion_detail_view, name='atencion-detail'),
	path('vehiculos/<int:id>/atenciones/<int:at>/editar/', atencion_update_view, name='atencion-update'),
	path('vehiculos/<int:id>/atenciones/<int:at>/eliminar/', atencion_delete_view, name='atencion-delete'),

	######## VEHICULOS/ATENCIONES/DETALLES #######

	path('vehiculos/<int:id>/atenciones/<int:at>/detalles/crear/', detalle_create_view, name='detalle-create'),
	path('vehiculos/<int:id>/atenciones/<int:at>/detalles/<int:de>/', detalle_detail_view, name='detalle-detail'),
	path('vehiculos/<int:id>/atenciones/<int:at>/detalles/<int:de>/eliminar/', detalle_delete_view, name='detalle-delete'),
	
]
