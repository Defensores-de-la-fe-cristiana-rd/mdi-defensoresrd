from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Noticias, Post, Contactanos, ImagenCarrusel
from .forms import CustomUserCreationForm, Post
from django.contrib import messages 
from django.contrib.auth import authenticate, login
from .forms import PostForm, NoticiasForm, ContactanosForm, ComentarioForm, CarruselForm
from django.contrib.auth.models import User
import xlsxwriter
from datetime import datetime

# Create your views here.



def Home(request):
    # Obtener todos los posts y noticias
    posteo = Post.objects.all().order_by('-created')
    news = Noticias.objects.all().order_by('-created')

    # Obtener todas las imágenes del carrusel
    imagenes_carrusel = ImagenCarrusel.objects.all().order_by('id')

    # Crear formulario de contacto
    form = ContactanosForm()

    # Procesar el envío del formulario de contacto
    if request.method == "POST":
        formulario = ContactanosForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Mensaje Enviado Satisfactoriamente")
            return redirect(to="Home")
        else:
            messages.error(request, "Error al enviar el mensaje. Por favor, revise los campos.")
            form = formulario

    # Pasar los datos al contexto
    data = {
        'Post': posteo,
        'Noticias': news,
        'imagenes_carrusel': imagenes_carrusel,
        'form': form,
    }

    return render(request, "ProyectoWebDefensores/home.html", data)




def Credo (request):
    return render(request, "ProyectoWebDefensores/credo.html")


def Cookies (request):
    current_year = datetime.now().year
    next_year = current_year + 1
    return render(request, "ProyectoWebDefensores/cookies.html", {'next_year': next_year})


def PoliticaPrivacidad (request):
    current_year = datetime.now().year
    next_year = current_year + 1
    return render(request, "ProyectoWebDefensores/politicaprivacidad.html", {'next_year': next_year})


def AvisoLegal (request):
    current_year = datetime.now().year
    next_year = current_year + 1
    return render(request, "ProyectoWebDefensores/avisolegal.html" , {'next_year': next_year})

@login_required(login_url='/accounts/login')
def Menu (request):
    return render(request, "registration/menu.html")


@login_required(login_url='/accounts/login') 
def Registro (request):
    data={
        'form': CustomUserCreationForm
    }

    if request.method == 'POST':
        formulario = CustomUserCreationForm(data=request.POST)
        if formulario.is_valid:
            formulario.save()
            user=authenticate(username= formulario.cleaned_data["username"], password=formulario.cleaned_data['password1'])
            login(request,user)
            messages.success(request, "Registro Completado Satisfactoriamente")
            return redirect(to='Menu')
        
        data["form"]=formulario
    return render (request, "registration/registro.html", data)





@login_required(login_url='/accounts/login')
def FormularioPosts(request):
    data = {'form': PostForm()}

    if request.method == "POST":
        formulario = PostForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            # Guarda el formulario pero no lo hace commit aún
            post = formulario.save(commit=False)
            # Asigna el usuario actual como el autor del post
            post.autor = request.user
            # Ahora sí, guarda el post en la base de datos
            post.save()
            messages.success(request, "Agregado Satisfactoriamente")
            return redirect(to="Posts")
        else:
            data["form"] = formulario
            
    return render(request, "ProyectoWebDefensores/formularioPost.html", data)



@login_required(login_url='/accounts/login') 
def ModificarPost(request, id):
    post = get_object_or_404(Post, id=id)
    data = {
        'form': PostForm(instance=post) 
    }
    if request.method=="POST":
        formulario=PostForm(data=request.POST, instance=post, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Modificado Satisfactoriamente")
            return redirect(to="Posts")
        data["form"] = formulario
    return render (request, "ProyectoWebDefensores/modificar_post.html", data)

@login_required(login_url='/accounts/login') 
def EliminarPost(request, id):
    posteo=get_object_or_404(Post, id=id)
    posteo.delete()
    messages.success(request, "Eliminado Satisfactoriamente")
    return redirect(to="Posts")

@login_required(login_url='/accounts/login') 
def MuestraPosts(request):
    listaPost = Post.objects.all().order_by('-created')
    data={
        'Post':listaPost
    }
    return render (request, "ProyectoWebDefensores/listar_post.html", data)




@login_required(login_url='/accounts/login') 
def listarNoticias(request):
    listaNoticia = Noticias.objects.all().order_by('-created')
    data={
        'Noticias':listaNoticia
    }
    return render (request, "ProyectoWebDefensores/listar_noticias.html", data)


@login_required(login_url='/accounts/login') 
def AgregaNoticia(request):
    data = {'form': NoticiasForm()}

    if request.method == "POST":
        formulario = NoticiasForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            # Guarda el formulario pero no lo hace commit aún
            noticia = formulario.save(commit=False)
            # Asigna el usuario actual como el autor de la noticia
            noticia.autor = request.user
            # Ahora sí, guarda la noticia en la base de datos
            noticia.save()
            messages.success(request, "Agregado Satisfactoriamente")
            return redirect(to="listaNoticias")
        else:
            data["form"] = formulario

    return render(request, "ProyectoWebDefensores/formularioNoticias.html", data)


@login_required(login_url='/accounts/login') 
def ModificarNoticia(request, id):
    noticia = get_object_or_404(Noticias, id=id)
    data = {
        'form': NoticiasForm(instance=noticia) 
    }
    if request.method=="POST":
        formulario=NoticiasForm(data=request.POST, instance=noticia, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Modificado Satisfactoriamente")
            return redirect(to="listaNoticias")
        data["form"] = formulario
    return render (request, "ProyectoWebDefensores/modificar_noticia.html", data)


def PublicaNoticias(request, id):
    news = get_object_or_404(Noticias, id=id)
    data = {'Noticias': [news]}
    return render(request, "ProyectoWebDefensores/noticias.html", data)



@login_required(login_url='/accounts/login') 
def EliminarNoticia(request, id):
    noticia=get_object_or_404(Noticias, id=id)
    noticia.delete()
    messages.success(request, "Eliminado Satisfactoriamente")
    return redirect(to="listaNoticias")



@login_required(login_url='/accounts/login') 
def ListarContacto(request):
    listaDeContacto = Contactanos.objects.all()
    data={
        'contactos':listaDeContacto
    }
    return render (request, "ProyectoWebDefensores/listaContacto.html", data)



@login_required(login_url='/accounts/login') 
def EliminarContactanos(request, id):
    contacto = get_object_or_404(Contactanos, id=id)
    contacto.delete()
    messages.success(request, "Eliminado Satisfactoriamente")
    return redirect('listaContactanos')




def exportar_contactos_a_excel(request):
    # Obtén la lista de contactos
    contactos = Contactanos.objects.all()

    # Crea un archivo Excel
    workbook = xlsxwriter.Workbook('contactos.xlsx')
    worksheet = workbook.add_worksheet()

    # Encabezados de columna
    headers = ['Nombre', 'Correo Electrónico', 'Teléfono', 'Mensaje']
    for col, header in enumerate(headers):
        worksheet.write(0, col, header)

    # Datos de los contactos
    for row, contacto in enumerate(contactos, start=1):
        worksheet.write(row, 0, contacto.nombre)
        worksheet.write(row, 1, contacto.correo)
        worksheet.write(row, 2, contacto.telefono)
        worksheet.write(row, 3, contacto.mensaje)

    # Cerrar el archivo Excel
    workbook.close()

    # Descargar el archivo Excel
    with open('contactos.xlsx', 'rb') as f:
        response = HttpResponse(f.read(), content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        response['Content-Disposition'] = 'attachment; filename=contactos.xlsx'
        return response

@login_required(login_url='/accounts/login') 
def user_list(request):
    users = User.objects.all()
    return render(request, 'registration/listaUsuario.html', {'users': users})



def ComentaPost (request, id):
    post = get_object_or_404(Post, id=id)
    form = ComentarioForm()
    data = {
        'Post': [post],
        'form': form,
        }
    return render(request, "ProyectoWebDefensores/Post.html", data)




@login_required(login_url='/accounts/login') 
def eliminarCarrousel(request, id):
    carrousel = get_object_or_404(ImagenCarrusel, id=id)
    carrousel.delete()
    messages.success(request, "Eliminado Satisfactoriamente")
    return redirect('listaCarrousel')




@login_required(login_url='/accounts/login') 
def VerCarrousel(request):
    listaDeCarrusel = ImagenCarrusel.objects.all().order_by('id')
    data={
        'Carrusel':listaDeCarrusel
    }
    return render (request, "ProyectoWebDefensores/listarCarrousel.html", data)

 


@login_required(login_url='/accounts/login') 
def modificarCarrousel(request, id):
    Carrousel = get_object_or_404(ImagenCarrusel, id=id)
    data = {
        'form': CarruselForm(instance=Carrousel) 
    }
    if request.method=="POST":
        formulario=CarruselForm(data=request.POST, instance=Carrousel, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Modificado Satisfactoriamente")
            return redirect(to="listaCarrousel")
        data["form"] = formulario
    return render (request, "ProyectoWebDefensores/modificarCarrousel.html", data)




@login_required(login_url='/accounts/login') 
def FormularioCarrousel(request):
    data={
        'form':CarruselForm()
    }

    if request.method=="POST":
        formulario=CarruselForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Agregado Satisfactoriamente")
            return redirect(to="listaCarrousel")
        else:
            data["form"]=formulario
            
    return render (request, "ProyectoWebDefensores/formularioCarrousel.html", data)

def error_404(request, exception):
    return render(request, 'ProyectoWebDefensores/404.html', status=404)

def error_500(request):
    return render(request, 'ProyectoWebDefensores/500.html', status=500)