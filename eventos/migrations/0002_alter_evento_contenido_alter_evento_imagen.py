# Generated by Django 4.0.5 on 2023-09-18 02:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eventos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evento',
            name='contenido',
            field=models.TextField(max_length=500),
        ),
        migrations.AlterField(
            model_name='evento',
            name='imagen',
            field=models.ImageField(upload_to='eventos'),
        ),
    ]
