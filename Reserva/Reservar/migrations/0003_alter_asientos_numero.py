# Generated by Django 4.0.5 on 2023-06-02 20:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Reservar', '0002_asientos_bus_ruta_reserva_disponibilidad_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='asientos',
            name='numero',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
