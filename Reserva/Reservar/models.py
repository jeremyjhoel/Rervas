from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver

class Cliente(models.Model):
    nombre = models.CharField(max_length=100, null=False)
    apellido = models.CharField(max_length=100, null=False)
    email = models.EmailField(max_length=100, null=False)
    telefono = models.CharField(max_length=20, blank=True)
    rut = models.CharField(max_length=200, null=False)

    def __str__(self):
        return self.nombre

class Ruta(models.Model):
    origen = models.CharField(max_length=100)
    destino = models.CharField(max_length=100)
    tiempoEstimado = models.CharField(max_length=100)

    def __str__(self):
        return self.destino

class Bus(models.Model):
    patente=models.CharField(max_length=50)
    cantidadAsientos = models.IntegerField()

    def __str__(self):
        return self.patente

class Asientos(models.Model):
    numero=models.IntegerField(blank=True, null=True)
    estado = models.BooleanField()
    bus = models.ForeignKey(Bus, on_delete=models.CASCADE)

def asignar_numero_asiento(sender, instance, **kwargs):
    if not instance.numero:
        # Obtener la cantidad de asientos del bus asociado
        cantidad_asientos = instance.bus.cantidadAsientos

        # Verificar si hay asientos disponibles
        asientos_ocupados = Asientos.objects.filter(bus=instance.bus).count()
        if asientos_ocupados < cantidad_asientos:
            # Calcular el siguiente número de asiento disponible
            siguiente_numero_asiento = asientos_ocupados + 1
            instance.numero = siguiente_numero_asiento
        else:
            # Si no hay asientos disponibles, establecer el número de asiento como None
            instance.numero = None

class Reserva(models.Model):
    fechaReserva=models.DateTimeField(null=False)
    cantidadPasajes = models.IntegerField(null=False)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    ruta = models.ForeignKey(Ruta, on_delete=models.CASCADE)
    bus = models.ForeignKey(Bus, on_delete=models.CASCADE)
    asiento = models.ForeignKey(Asientos, on_delete=models.CASCADE)
    def __str__(self):
        return self.fechaReserva

class Disponibilidad(models.Model):
    bus = models.ForeignKey(Bus, on_delete=models.CASCADE, related_name='disponibilidades_bus')
    asiento = models.ForeignKey(Asientos, on_delete=models.CASCADE, related_name='disponibilidades_asiento')
    ruta = models.ForeignKey(Ruta, on_delete=models.CASCADE, related_name='disponibilidades_ruta')
    horario = models.TimeField()
    fecha = models.DateField()
    disponible = models.BooleanField()
    def __str__(self):
        return self.horario



# Create your models here.
