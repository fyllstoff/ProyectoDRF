# Generated by Django 4.2 on 2024-11-30 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventarioAPP', '0002_producto_categoria_producto_disponible_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rut', models.CharField(max_length=12, unique=True)),
                ('nombres', models.CharField(max_length=100)),
                ('apellidos', models.CharField(max_length=100)),
                ('fecha_nacimiento', models.DateField()),
                ('hora_ingreso', models.TimeField()),
                ('diagnostico', models.TextField()),
                ('doctor', models.CharField(max_length=100)),
                ('estado', models.CharField(max_length=50)),
            ],
        ),
        migrations.DeleteModel(
            name='Producto',
        ),
    ]
