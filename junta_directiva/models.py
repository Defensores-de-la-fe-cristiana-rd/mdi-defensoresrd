from django.db import models

# Create your models here.



class junta_directiva(models.Model):
    nombre=models.CharField(max_length=50, null=True)
    ocupacion=models.CharField(max_length=50, null=True)
    contenido=models.TextField(max_length=1500, null=True)
    imagen=models.ImageField(upload_to="junta_directiva", null=True)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name='Junta de Directores'

    def __str__(self):
        return self.ocupacion 