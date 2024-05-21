from django.shortcuts import render, redirect, get_object_or_404
from .models import junta_directiva
from .forms import DirectivaForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.



def Junta_Directiva (request):
    junta=junta_directiva.objects.all()
    return render(request, "Junta_Directiva/junta_directiva.html", {"junta_directiva":junta})

@login_required(login_url='/accounts/login')
def Formulario_Junta (request):
    data={
        'form':DirectivaForm()
    }

    if request.method== 'POST':
        formulario=DirectivaForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
        else:
            data["form"]=formulario
    return render (request, "junta_directiva/formularioDirectiva.html", data)


@login_required(login_url='/accounts/login') 
def MuestraJunta(request):
    lista=junta_directiva.objects.all()
    data={
        'directiva':lista
    }
    return render (request, "junta_directiva/lista_junta.html", data)

@login_required(login_url='/accounts/login')
def ModificaDirectiva (request, id):
    junta=get_object_or_404(junta_directiva,id=id)
    data={
        'form': DirectivaForm (instance=junta)
    }

    if request.method=='POST':
        formulario=DirectivaForm(data=request.POST,instance=junta, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Modificado Satisfactoriamente")
            return redirect(to="muestra_junta")
        data["form"]=formulario
    return render (request, "junta_directiva/modificar.html", data)
