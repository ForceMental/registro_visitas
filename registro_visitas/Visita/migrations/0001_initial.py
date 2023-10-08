# Generated by Django 4.2.6 on 2023-10-08 18:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Cliente', '0001_initial'),
        ('Empleado', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Visita',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_visita', models.CharField(choices=[('F', 'En frío'), ('A', 'Agendada')], default='F', max_length=1)),
                ('estado_visita', models.CharField(choices=[('P', 'Pendiente'), ('R', 'Realizada'), ('C', 'Cancelada')], default='P', max_length=1)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Cliente.cliente')),
                ('empleado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Empleado.empleado')),
            ],
        ),
    ]