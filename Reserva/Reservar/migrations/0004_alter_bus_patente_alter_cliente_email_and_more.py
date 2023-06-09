# Generated by Django 4.2.1 on 2023-06-14 21:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Reservar', '0003_alter_asientos_numero'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bus',
            name='patente',
            field=models.CharField(max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='email',
            field=models.EmailField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='rut',
            field=models.CharField(max_length=200, unique=True),
        ),
    ]
