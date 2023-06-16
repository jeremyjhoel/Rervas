from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404

from .models import Cliente, Bus
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .forms import BusForm
from .forms import RutaForm


def index(request):
    return render(request, 'index.html')

def formBus(request):
    buses = Bus.objects.all()
    if request.method == 'POST':
        form = BusForm(request.POST)
        if form.is_valid():
            bus = form.save(commit=False)
            bus.author = request.user
            bus.save()
            messages.success(request, 'La publicación fue guardada exitosamente')
            return redirect('formBus')  # Reemplaza 'nombre-de-la-vista' por el nombre de la vista a la que quieres redirigir
        else:
            messages.error(request, 'Ha ocurrido un error al guardar la publicación')
    else:
        form = BusForm()
    return render(request, 'buses/formBus.html', {'buses': buses, 'formulario': form})

def editarBus(request, bus_id):
    bus = get_object_or_404(Bus, id=bus_id)
    if request.method == 'POST':
        form = BusForm(request.POST, instance=bus)
        if form.is_valid():
            form.save()
            messages.success(request, 'El bus fue actualizado exitosamente')
            return redirect('formBus')  # Reemplaza 'nombre-de-la-vista' por el nombre de la vista a la que quieres redirigir
        else:
            messages.error(request, 'Ha ocurrido un error al actualizar el bus')
    else:
        form = BusForm(instance=bus)
    return render(request, 'buses/editarBus.html', {'formulario': form})

def eliminarBus(request, bus_id):
    bus = get_object_or_404(Bus, id=bus_id)
    if request.method == 'POST':
        bus.delete()
        messages.success(request, 'El bus fue eliminado exitosamente')
        return redirect('formBus')  # Reemplaza 'nombre-de-la-vista' por el nombre de la vista a la que quieres redirigir
    return render(request, 'buses/eliminarBus.html', {'bus': bus})





def login(request):
    return render(request, 'blog/login.html')





class BusListView(ListView):
    model = Bus
    template_name = 'buses/bus_list.html'
    context_object_name = 'buses'
    success_url = '/buses/'

class BusCreateView(CreateView):
    model = Bus
    form_class = BusForm
    template_name = 'buses/bus_create.html'
    success_url = '/buses/'

class BusUpdateView(UpdateView):
    model = Bus
    form_class = BusForm
    template_name = 'buses/bus_update.html'
    success_url = '/buses/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['bus_id'] = self.object.id
        return context

class BusDeleteView(DeleteView):
    model = Bus
    template_name = 'buses/bus_delete.html'
    success_url = '/buses/'


#Esto para las rutas:

class RutaListView(ListView):
    model = Ruta
    template_name = 'rutas/ruta_list.html'
    context_object_name = 'rutas'
    success_url = '/rutas/'


class RutaCreateView(CreateView):
    model = Ruta
    form_class = RutaForm
    template_name = 'rutas/ruta_create.html'
    success_url = '/rutas/'


class RutaUpdateView(UpdateView):
    model = Ruta
    form_class = RutaForm
    template_name = 'rutas/ruta_update.html'
    success_url = '/rutas/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['ruta_id'] = self.object.id
        return context


class RutaDeleteView(DeleteView):
    model = Ruta
    template_name = 'rutas/ruta_delete.html'
    success_url = '/rutas/'

