from django.db import models
from django.contrib.auth.models import User
import json

# Create your models here.
class Noticias(models.Model):
    tituloPequeno=models.CharField(max_length=120, verbose_name="Título")
    tituloGrande=models.CharField(max_length=250, verbose_name="Título Grande")
    contenidoPequeno=models.TextField(max_length=500, verbose_name="Contenido")
    contenido=models.TextField(max_length=2500, verbose_name="Contenido Grande")
    imagen=models.ImageField(upload_to='NoticiaUno')
    autor=models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)
    
 
    class Meta:
        verbose_name='Noticias'
        verbose_name_plural='Noticias'
    
    def __str__(self):
        return self.tituloGrande
    




    


class Post (models.Model):
    titulo=models.CharField(max_length=50)
    contenido=models.TextField(max_length=500)
    imagen=models.ImageField(upload_to='Blog', null=True, blank=True)
    autor=models.ForeignKey(User, on_delete=models.CASCADE)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)


    class Meta:
        verbose_name='Post'
        verbose_name_plural='Posts'
    
    def __str__(self):
        return f"{self.titulo} - {self.autor.username}"


class Contactanos(models.Model):
    nombre=models.CharField(max_length=100)
    telefono=models.CharField(max_length=100, verbose_name="Teléfono") 
    correo=models.EmailField(max_length=100, verbose_name="Correo Electrónico")
    mensaje=models.TextField(max_length=2500)
   
    class Meta:
        verbose_name='Contactano'
        verbose_name_plural='Contactanos'
    
    def __str__(self):
        return self.nombre
    


class Comentario(models.Model):
    nombre = models.CharField(max_length=100)
    correo = models.EmailField(verbose_name="Correo Electrónico")
    comentario = models.TextField(max_length=2500)

    class Meta:
        verbose_name='Comentario'
        verbose_name_plural='Comentarios'
    
    def __str__(self):
        return self.nombre
    
 
class ImagenCarrusel(models.Model):
    titulo = models.CharField(max_length=100)
    contenido = models.TextField()
    imagen = models.ImageField(upload_to='carrusel/')  

    def __str__(self):
        return self.titulo