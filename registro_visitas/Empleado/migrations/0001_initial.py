# Generated by Django 4.2.6 on 2023-10-08 18:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_empleado', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
                ('stock_disponible', models.PositiveIntegerField(default=0)),
                ('tipo_empleado', models.CharField(choices=[('J', 'Jefe'), ('E', 'Ejecutivo')], max_length=1)),
                ('jefe', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='subordinados', to='Empleado.empleado')),
            ],
        ),
    ]
