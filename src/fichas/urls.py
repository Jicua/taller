from django.urls import path
from .views import (
	fichas_home_view,

	cliente_list_view,
	cliente_create_view,
	cliente_detail_view,
	cliente_update_view,
	cliente_delete_view,

	vehiculo_list_view,
	vehiculo_create_view,
	vehiculo_detail_view,
	vehiculo_update_view,
	vehiculo_delete_view
	)

app_name = 'fichas'
urlpatterns = [
	path('', fichas_home_view, name='fichas'),

	path('clientes/', cliente_list_view, name='cliente-list'),
	path('clientes/crear/', cliente_create_view, name='cliente-create'),
	path('clientes/<int:id>/', cliente_detail_view, name='cliente-detail'),
	path('clientes/<int:id>/editar/', cliente_update_view, name='cliente-update'),
	path('clientes/<int:id>/eliminar/', cliente_delete_view, name='cliente-delete'),

	path('vehiculos/', vehiculo_list_view, name='vehiculo-list'),
	path('vehiculos/crear/', vehiculo_create_view, name='vehiculo-create'),
	path('vehiculos/<int:id>/', vehiculo_detail_view, name='vehiculo-detail'),
	path('vehiculos/<int:id>/editar/', vehiculo_update_view, name='vehiculo-update'),
	path('vehiculos/<int:id>/eliminar/', vehiculo_delete_view, name='vehiculo-delete'),
]