from django.shortcuts import render
from .models import Cliente

def mostrar_clientes(request):
    clientes = Cliente.objects.all()
    return render(request, 'clientes.html', {'clientes': clientes})



# Create your views here.
