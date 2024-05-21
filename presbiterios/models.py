from django.db import models

# Create your models here.


class PresbiteriosDef(models.Model):
    titulo=models.CharField(max_length=100)
    contenido=models.TextField(max_length=1000)
    imagen=models.ImageField(upload_to='presbiterios')
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name='Presbiterio'
        verbose_name_plural='Presbiterios'
    
    def __str__(self):
        return self.titulo