from django.urls import path
from . import views
from django import urls
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
     
    path ('', views.Eventos, name="Eventos"),
    path ('FormularioEvento' ,views.FormularioEvento, name="formularioEvento" ),
    path ('listar_eventos', views.MuestraEventos, name="listar_eventos"),
    path ('modificar_evento/<id>', views.ModificarEventos, name="modificar_eventos"),
    path ('eliminar_evento/<id>', views.EliminarEvento, name="elimininarEvento")
]



if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)