# Generated by Django 4.2.6 on 2023-10-28 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Procesos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero_proceso', models.CharField(max_length=255)),
                ('nombre_proceso', models.CharField(max_length=255)),
                ('tipo_proceso', models.CharField(max_length=255)),
                ('fecha_apertura', models.DateTimeField()),
                ('unidad_ejecutora', models.IntegerField()),
            ],
        ),
    ]