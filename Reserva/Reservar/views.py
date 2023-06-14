from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required

from .models import Cliente, Bus
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .forms import BusForm


def index(request):
    posts = Bus.objects.all()
    if request.method == 'POST':
        post_form = BusForm(request.POST)
        if post_form.is_valid():
            temp = post_form.save(commit=False);
            temp.author = request.user;
            temp.save()
            messages.success(request, 'La publicación fue guardada exitosamente')
        else:
            messages.error(request, 'Ha ocurrido un error al guardar la publicación')
    bus_form = BusForm()
    return render(request, 'index.html', {'bus': posts, 'formulario': bus_form})

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
