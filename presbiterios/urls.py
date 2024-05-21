from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views


urlpatterns = [
      
    path ('', views.Presbiterios, name="Presbiterios"),
    path ('listar_presbiterios', views.MuestraPresbiterios, name="listar_presbiterios"),   
    path ('FormularioPresbiterio' ,views.FormularioPresbiterios, name="formularioPresbiterios" ),
    path ('modificar_presbiterio/<id>', views.ModificarPresbiterio, name="modificar_presbiterio"),
    path ('eliminar_presbiterio/<id>', views.EliminarPresbiterio, name="eliminar_presbiterio")
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)