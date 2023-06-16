from django import forms
from .models import Bus
from .models import Ruta

class BusForm(forms.ModelForm):

    class Meta:
        model = Bus
        fields = ('patente','cantidadAsientos')

class RutaForm(forms.ModelForm):

    class Meta:
        model = Ruta
        fields = ('origen', 'destino', 'tiempoEstimado')
