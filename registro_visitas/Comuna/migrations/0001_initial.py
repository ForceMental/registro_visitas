# Generated by Django 4.2.6 on 2023-10-08 02:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Region', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comuna',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_comuna', models.CharField(max_length=255)),
                ('region', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Region.region')),
            ],
        ),
    ]