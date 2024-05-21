from django.db import models

# Create your models here.

 
class NosotrosDef(models.Model):
    titulo=models.CharField(max_length=100)
    contenido=models.TextField(max_length=5000)
    imagen=models.ImageField(upload_to='nosotros')
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name='Nosotro'
        verbose_name_plural='Nosotros'
    
    def __str__(self):
        return self.titulo
    

class Imagen(models.Model):
    titulo = models.CharField(max_length=100)
    contenido=models.TextField(max_length=200)
    imagen = models.ImageField(upload_to='Campamento/')

    class Meta:
        verbose_name='Imagen'
        verbose_name_plural='Imagenes'
    
    def __str__(self):
        return self.titulo


class Archivo(models.Model):
    nombre = models.CharField(max_length=100)
    contenido=models.TextField(max_length=200)
    archivo = models.FileField(upload_to='archivos/')

    def __str__(self):
        return self.nombre