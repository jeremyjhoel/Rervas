"""Reserva URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
#from Reservar.views import BusListView, BusCreateView, BusUpdateView, BusDeleteView
from Reservar.views import index, formBus, editarBus, eliminarBus
from Reservar.views import RutaListView, RutaCreateView, RutaUpdateView, RutaDeleteView

app_name = 'Reservar'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', index, name='index'),
    path('', index, name='index'),
    path("accounts/", include("django.contrib.auth.urls")),
    path('formBus/', formBus, name='formBus'),
    path('buses/editar/<int:bus_id>/', editarBus, name='editar_bus'),
    path('buses/eliminar/<int:bus_id>/', eliminarBus, name='eliminar_bus'),



    #path('buses/', BusListView.as_view(), name='bus_list'),
    #path('buses/create/', BusCreateView.as_view(), name='bus_create'),
    #path('buses/update/<int:pk>/', BusUpdateView.as_view(), name='bus_update'),
    #path('buses/delete/<int:pk>/', BusDeleteView.as_view(), name='bus_delete'),

    path('rutas/', RutaListView.as_view(), name='ruta_list'),
    path('rutas/create/', RutaCreateView.as_view(), name='ruta_create'),
    path('rutas/update/<int:pk>/', RutaUpdateView.as_view(), name='ruta_update'),
    path('rutas/delete/<int:pk>/', RutaDeleteView.as_view(), name='ruta_delete'),
]
