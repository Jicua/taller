from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from .views import (
	home_view,
	contact_view
	)
from fichas.views import revisar_view

urlpatterns = [
	path('', home_view, name='home'),
	path('contacto/', contact_view, name='contacto'),
	path('revisar/', revisar_view, name='revisar'),
]