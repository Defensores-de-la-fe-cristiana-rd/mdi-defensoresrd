# Generated by Django 4.0.5 on 2022-10-28 02:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='junta_directiva',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ocupacion', models.CharField(max_length=50)),
                ('contenido', models.CharField(max_length=500)),
                ('imagen', models.ImageField(upload_to='')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Junta de Directores',
            },
        ),
    ]
