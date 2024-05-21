from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views


urlpatterns = [
    
    
    path ('', views.Departamentos, name="Departamentos"),
    path ('listar_departamentos', views.MuestraDepartamentos, name="listar_departamentos"),
    path ('FormularioDepartamentos' ,views.FormularioDepartamentos, name="formularioDepartamentos" ),
    path ('modificar_departamento/<id>', views.ModificarDepartamento, name="modificar_departamento"),
    path ('eliminar_departamento/<id>', views.EliminarDepartamento, name="eliminar_departamento")
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)