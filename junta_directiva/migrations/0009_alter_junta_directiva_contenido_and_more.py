# Generated by Django 4.0.5 on 2023-09-29 02:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('junta_directiva', '0008_alter_junta_directiva_ocupacion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='junta_directiva',
            name='contenido',
            field=models.TextField(max_length=1500, null=True),
        ),
        migrations.AlterField(
            model_name='junta_directiva',
            name='ocupacion',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
