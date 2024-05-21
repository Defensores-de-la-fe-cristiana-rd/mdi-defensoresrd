from django.urls import path
from django import urls
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [ 
     
    
    path ('', views.Junta_Directiva, name="Junta_Directiva"),
    path ('formulario_directiva' ,views.Formulario_Junta, name="formulario" ),
    path ('listar_directiva', views.MuestraJunta, name="muestra_junta"),
    path ('modificar_directiva/<id>', views.ModificaDirectiva, name="modificacion_directiva")
]




if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)