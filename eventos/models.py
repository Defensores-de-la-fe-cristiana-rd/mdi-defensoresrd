from django.db import models

# Create your models here.
class Evento(models.Model):
    titulo=models.CharField(max_length=50)
    contenido=models.TextField(max_length=1500)
    imagen=models.ImageField(upload_to='eventos')
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name='Evento'
        verbose_name_plural='Evento'
    
    def __str__(self):
        return self.titulo
