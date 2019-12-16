from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from .views import (
	horas_home_view,
	reserva_view,
	admin_view,
	admin_view_todas
	)

app_name = 'horas'
urlpatterns = [
	path('', horas_home_view, name="horas"),
	path('reserva', reserva_view, name="reserva"),
	path('admin', admin_view, name="admin"),
	path('todas', admin_view_todas, name="todas")
]