from django.shortcuts import render, redirect, get_object_or_404
from .models import PresbiteriosDef
from .forms import PresbiteriosDefForm
from django.contrib import messages 
from django.contrib.auth.decorators import login_required
# Create your views here.


def Presbiterios (request):
    presb = PresbiteriosDef.objects.all()
    return render(request, "presbiterios/presbiterios.html", {"PresbiteriosDef": presb})

@login_required(login_url='/accounts/login') 
def MuestraPresbiterios(request):
    presbiLista = PresbiteriosDef.objects.all()
    data={
        'PresbiteriosDef':presbiLista
    }
    return render (request, "presbiterios/lista_presbiterio.html", data)


@login_required(login_url='/accounts/login') 
def FormularioPresbiterios(request):
    data={
        'form':PresbiteriosDefForm()
    }

    if request.method=="POST":
        formulario=PresbiteriosDefForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Agregado Satisfactoriamente")
            return redirect(to="listar_presbiterios")
        else:
            data["form"]=formulario
            
    return render (request, "presbiterios/formularioPresbiterio.html", data)
 

@login_required(login_url='/accounts/login') 
def ModificarPresbiterio(request, id):
    presbiterio = get_object_or_404(PresbiteriosDef, id=id)
    data = {
        'form': PresbiteriosDefForm(instance=presbiterio) 
    }
    if request.method=="POST":
        formulario=PresbiteriosDefForm(data=request.POST, instance=presbiterio, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Modificado Satisfactoriamente")
            return redirect(to="listar_presbiterios")
        data["form"] = formulario
    return render (request, "presbiterios/modificar.html", data)

@login_required(login_url='/accounts/login') 
def EliminarPresbiterio(request, id):
    presbiterios=get_object_or_404(PresbiteriosDef, id=id)
    presbiterios.delete()
    messages.success(request, "Eliminado Satisfactoriamente")
    return redirect(to="listar_presbiterios")