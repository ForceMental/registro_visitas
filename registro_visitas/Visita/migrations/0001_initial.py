# Generated by Django 4.2.4 on 2023-10-11 02:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Cliente', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Visita',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_visita', models.CharField(choices=[('F', 'En frío'), ('A', 'Agendada')], default='F', max_length=1)),
                ('empleado_nombre', models.CharField(max_length=255)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Cliente.cliente')),
            ],
        ),
    ]
