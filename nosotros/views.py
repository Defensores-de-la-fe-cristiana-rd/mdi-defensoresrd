from django.shortcuts import render, redirect, get_object_or_404
from .models import NosotrosDef, Imagen, Archivo
from .forms import NosotrosDefForm, ImagenForm, ArchivoForm
from django.contrib import messages 
from django.contrib.auth.decorators import login_required
# Create your views here.

 
def Nosotros (request):
    noss = NosotrosDef.objects.all()
    imagenes = Imagen.objects.all()
    archivos = Archivo.objects.all()
    data ={
        "NosotrosDef":noss,
        "campamento":imagenes,
        "archivo":archivos
    }
    return render(request, "nosotros/nosotros.html", data)

@login_required(login_url='/accounts/login') 
def MuestraNosotros(request):
    nosLista = NosotrosDef.objects.all()
    data={
        'NosotrosDef':nosLista
    }
    return render (request, "nosotros/lista_nosotros.html", data)


@login_required(login_url='/accounts/login') 
def FormularioNosotros(request):
    data={
        'form':NosotrosDefForm()
    }

    if request.method=="POST":
        formulario=NosotrosDefForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Agregado Satisfactoriamente")
            return redirect(to="listar_nosotros")
        else:
            data["form"]=formulario
            
    return render (request, "nosotros/formularioNosotros.html", data)


@login_required(login_url='/accounts/login') 
def ModificarNosotros(request, id):
    nosotross = get_object_or_404(NosotrosDef, id=id)
    data = {
        'form': NosotrosDefForm(instance=nosotross) 
    }
    if request.method=="POST":
        formulario=NosotrosDefForm(data=request.POST, instance=nosotross, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Modificado Satisfactoriamente")
            return redirect(to="listar_nosotros")
        data["form"] = formulario
    return render (request, "nosotros/modificar.html", data)

@login_required(login_url='/accounts/login') 
def EliminarNosotros(request, id):
    todosnosotros=get_object_or_404(NosotrosDefForm, id=id)
    todosnosotros.delete()
    messages.success(request, "Eliminado Satisfactoriamente")
    return redirect(to="listar_nosotros")


@login_required(login_url='/accounts/login') 
def MuestraGaleria(request):
    galLista = Imagen.objects.all()
    data={
        'Imagen':galLista
    }
    return render (request, "nosotros/listar_galeria.html", data)


@login_required(login_url='/accounts/login') 
def FormularioGaleria(request):
    data={
        'form':ImagenForm()
    }

    if request.method=="POST":
        formulario=ImagenForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Agregado Satisfactoriamente")
            return redirect(to="listar_galeria")
        else:
            data["form"]=formulario
            
    return render (request, "nosotros/formularioGaleria.html", data)


@login_required(login_url='/accounts/login') 
def ModificarGaleria(request, id):
    galerias = get_object_or_404(Imagen, id=id)
    data = {
        'form': ImagenForm(instance=galerias) 
    }
    if request.method=="POST":
        formulario=ImagenForm(data=request.POST, instance=galerias, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Modificado Satisfactoriamente")
            return redirect(to="listar_galeria")
        data["form"] = formulario
    return render (request, "nosotros/modificar_galeria.html", data)
 
@login_required(login_url='/accounts/login') 
def EliminarGaleria(request, id):
    todosgaleria=get_object_or_404(Imagen, id=id)
    todosgaleria.delete()
    messages.success(request, "Eliminado Satisfactoriamente")
    return redirect(to="listar_galeria")



@login_required(login_url='/accounts/login') 
def eliminarArchivo(request, id):
    archivo = get_object_or_404(Archivo, id=id)
    archivo.delete()
    messages.success(request, "Eliminado Satisfactoriamente")
    return redirect('listarArchivos')




@login_required(login_url='/accounts/login') 
def VerArchivos(request):
    listaDeArchivos = Archivo.objects.all()
    data={
        'Archivo':listaDeArchivos
    }
    return render (request, "Nosotros/listarArchivos.html", data)




@login_required(login_url='/accounts/login') 
def ModificarArchivo(request, id):
    archivo = get_object_or_404(Archivo, id=id)
    data = {
        'form': ArchivoForm(instance=archivo) 
    }
    if request.method=="POST":
        formulario=ArchivoForm(data=request.POST, instance=Archivo, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Modificado Satisfactoriamente")
            return redirect(to="listarArchivos")
        data["form"] = formulario
    return render (request, "Nosotros/ModificarArchivo.html", data)




@login_required(login_url='/accounts/login') 
def formularioArchivo(request):
    data={
        'form':ArchivoForm()
    }

    if request.method=="POST":
        formulario=ArchivoForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Agregado Satisfactoriamente")
            return redirect(to="listarArchivos")
        else:
            data["form"]=formulario
            
    return render (request, "Nosotros/formularioArchivo.html", data)