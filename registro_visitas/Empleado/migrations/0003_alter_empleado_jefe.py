# Generated by Django 4.2.6 on 2023-10-08 18:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Empleado', '0002_alter_empleado_jefe_alter_empleado_stock_disponible'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empleado',
            name='jefe',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Empleado.empleado'),
        ),
    ]