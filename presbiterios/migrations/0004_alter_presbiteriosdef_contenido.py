# Generated by Django 4.0.5 on 2023-11-19 23:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('presbiterios', '0003_rename_presbiterios_presbiteriosdef'),
    ]

    operations = [
        migrations.AlterField(
            model_name='presbiteriosdef',
            name='contenido',
            field=models.TextField(max_length=1000),
        ),
    ]
