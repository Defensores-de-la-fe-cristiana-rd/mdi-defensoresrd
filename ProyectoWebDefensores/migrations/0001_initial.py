# Generated by Django 4.0.5 on 2023-11-10 02:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NoticiaDos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tituloGrande', models.CharField(max_length=250)),
                ('tituloPequeno', models.CharField(max_length=120)),
                ('contenidoPequeno', models.CharField(max_length=500)),
                ('contenido', models.CharField(max_length=1000)),
                ('imagen', models.ImageField(upload_to='NoticiaUno')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'NoticiaDos',
                'verbose_name_plural': 'NoticiaDos',
            },
        ),
        migrations.CreateModel(
            name='NoticiaTres',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tituloPequeno', models.CharField(max_length=120)),
                ('tituloGrande', models.CharField(max_length=250)),
                ('contenidoPequeno', models.CharField(max_length=500)),
                ('contenido', models.CharField(max_length=1000)),
                ('imagen', models.ImageField(upload_to='NoticiaTres')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'NoticiaTres',
                'verbose_name_plural': 'NoticiaTres',
            },
        ),
        migrations.CreateModel(
            name='NoticiaUno',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tituloPequeno', models.CharField(max_length=120)),
                ('tituloGrande', models.CharField(max_length=250)),
                ('contenidoPequeno', models.CharField(max_length=500)),
                ('contenido', models.CharField(max_length=1000)),
                ('imagen', models.ImageField(upload_to='NoticiaUno')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'NoticiaUno',
                'verbose_name_plural': 'NoticiaUnos',
            },
        ),
    ]
