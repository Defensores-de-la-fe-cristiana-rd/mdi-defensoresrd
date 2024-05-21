from django.shortcuts import render, redirect, get_object_or_404
from .models import Evento
from .forms import EventoForm
from django.contrib import messages 
from django.contrib.auth.decorators import login_required
 
# Create your views here.

def Eventos (request):
    event=Evento.objects.all().order_by('-created')
    return render(request, "eventos/eventos.html", {"Evento":event})

@login_required(login_url='/accounts/login') 
def MuestraEventos(request):
    eventoLista = Evento.objects.all().order_by('-created')
    data={
        'Evento':eventoLista
    }
    return render (request, "eventos/lista_evento.html", data)

@login_required(login_url='/accounts/login') 
def FormularioEvento(request):
    data={
        'form':EventoForm()
    }

    if request.method=="POST":
        formulario=EventoForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Agregado Satisfactoriamente")
            return redirect(to="listar_eventos")
        else:
            data["form"]=formulario
            
    return render (request, "eventos/formularioEvento.html", data)

@login_required(login_url='/accounts/login') 
def ModificarEventos(request, id):
    evento = get_object_or_404(Evento, id=id)
    data = {
        'form': EventoForm(instance=evento) 
    }
    if request.method=="POST":
        formulario=EventoForm(data=request.POST, instance=evento, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Modificado Satisfactoriamente")
            return redirect(to="listar_eventos")
        data["form"] = formulario
    return render (request, "eventos/modificar.html", data)

@login_required(login_url='/accounts/login') 
def EliminarEvento(request, id):
    evento=get_object_or_404(Evento, id=id)
    evento.delete()
    messages.success(request, "Eliminado Satisfactoriamente")
    return redirect(to="listar_eventos")




