from django.shortcuts import render, redirect, get_object_or_404
from .models import DepartamentosDef
from .forms import DepartamentosDefForm
from django.contrib import messages 
from django.contrib.auth.decorators import login_required
# Create your views here.


def Departamentos (request):
    dept = DepartamentosDef.objects.all()
    return render(request, "departamentos/departamentos.html", {"DepartamentosDef":dept})


@login_required(login_url='/accounts/login') 
def MuestraDepartamentos(request):
    depLista = DepartamentosDef.objects.all()
    data={
        'DepartamentosDef':depLista
    }
    return render (request, "departamentos/lista_departamentos.html", data)



@login_required(login_url='/accounts/login') 
def FormularioDepartamentos(request):
    data={
        'form':DepartamentosDefForm()
    }

    if request.method=="POST":
        formulario=DepartamentosDefForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Agregado Satisfactoriamente")
            return redirect(to="listar_departamentos")
        else:
            data["form"]=formulario
            
    return render (request, "departamentos/formularioDepartamentos.html", data)


@login_required(login_url='/accounts/login') 
def ModificarDepartamento(request, id):
    departamento = get_object_or_404(DepartamentosDef, id=id)
    data = {
        'form': DepartamentosDefForm(instance=departamento) 
    }
    if request.method=="POST":
        formulario=DepartamentosDefForm(data=request.POST, instance=departamento, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Modificado Satisfactoriamente")
            return redirect(to="listar_departamentos")
        data["form"] = formulario
    return render (request, "departamentos/modificar.html", data)

@login_required(login_url='/accounts/login') 
def EliminarDepartamento(request, id):
    departamento=get_object_or_404(DepartamentosDef, id=id)
    departamento.delete()
    messages.success(request, "Eliminado Satisfactoriamente")
    return redirect(to="listar_departamentos")