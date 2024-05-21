from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views


urlpatterns = [
    path ('', views.Nosotros, name="Nosotros"),
    path ('listar_nosotros', views.MuestraNosotros, name="listar_nosotros"),   
    path ('FormularioNosotros' ,views.FormularioNosotros, name="formularioNosotros" ),
    path ('modificar_nosotros/<id>', views.ModificarNosotros, name="modificar_nosotros"),
    path ('eliminar_nosotros/<id>', views.EliminarNosotros, name="eliminar_nosotros"),
    path ('listar_galeria', views.MuestraGaleria, name="listar_galeria"),   
    path ('FormularioGaleria' ,views.FormularioGaleria, name="formularioGaleria" ),
    path ('modificar_galeria/<id>', views.ModificarGaleria, name="modificar_galeria"),
    path ('eliminar_galeria/<id>', views.EliminarGaleria, name="eliminar_galeria"),
    path ('listarArchivos/', views.VerArchivos, name='listarArchivos'),
    path ('AgregarArchivo/', views.formularioArchivo, name='AgregarArchivo'),
    path ('ModificarArchivo/<id>', views.ModificarArchivo, name="ModificarArchivo"),
    path ('eliminarArchivo/<id>', views.eliminarArchivo, name="eliminarArchivo"),

]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)