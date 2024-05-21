from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from django.urls import reverse
from django.conf.urls import handler404, handler500
from django.http import HttpResponseNotFound, HttpResponseServerError
from ProyectoWebDefensores import views


urlpatterns = [
     
    path ('', views.Home, name="Home"),
    path ('Credo', views.Credo, name="Credo"),
    path ('Cookies', views.Cookies, name="Cookies"),
    path ('PoliticaPrivacidad', views.PoliticaPrivacidad, name="PoliticaPrivacidad"),
    path ('AvisoLegal', views.AvisoLegal, name="AvisoLegal"),
    path ('Menu', views.Menu, name="Menu"),
    path ('Registro', views.Registro, name="Registro"),
    path ('Noticias/<id>', views.PublicaNoticias, name="Noticias"),
    path ('Posts', views.MuestraPosts, name="Posts"),
    path ('Agregar_Post', views.FormularioPosts, name="Agregar_Post"),
    path ('modificar_post/<id>', views.ModificarPost, name="modificar_post"),
    path ('eliminar_post/<id>', views.EliminarPost, name="eliminar_post"),
    path ('listaNoticias', views.listarNoticias, name="listaNoticias"),
    path ('Agregar_Noticia', views.AgregaNoticia, name="Agregar_Noticia"),
    path ('modificar_noticia/<id>', views.ModificarNoticia, name="modificar_Noticia"),
    path ('eliminar_noticia/<id>', views.EliminarNoticia, name="eliminar_Noticia"),
    path ('listaContactanos', views.ListarContacto, name="listaContactanos"),
    path ('eliminar_contactanos/<id>', views.EliminarContactanos, name="eliminar_contactanos"),
    path ('exportar_contactos_a_excel/', views.exportar_contactos_a_excel, name='exportar_contactos_a_excel'),
    path ('listaUsuarios/', views.user_list, name='listaUsuarios'),
    path ('comentaPost/<id>', views.ComentaPost, name='comentaPost'),

    path ('listaCarrousel/', views.VerCarrousel, name='listaCarrousel'),
    path ('AgregarCarrousel/', views.FormularioCarrousel, name='AgregarCarrousel'),
    path ('modificarCarrousel/<id>', views.modificarCarrousel, name="modificarCarrousel"),
    path ('eliminarCarrousel/<id>', views.eliminarCarrousel, name="eliminarCarrousel"),
    
]
handler404 = 'ProyectoWebDefensores.views.error_404'
handler500 = 'ProyectoWebDefensores.views.error_500'


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)