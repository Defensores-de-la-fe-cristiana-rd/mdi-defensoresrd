from django.db import models

# Create your models here.


class DepartamentosDef(models.Model):
    titulo=models.CharField(max_length=100)
    contenido=models.TextField(max_length=5000)
    imagen=models.ImageField(upload_to='departamentos')
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name='Departamento'
        verbose_name_plural='Departamentos'
    
    def __str__(self):
        return self.titulo