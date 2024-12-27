from django.shortcuts import render,redirect
from .models import Seleccion
from camisetas.forms import SeleccionForm
from django.contrib.auth.decorators import login_required

# Create your views here.

def lista_seleccion(request):
    listas=Seleccion.objects.all()
    return render (request,'camisetas/selecciones.html',{"listas":listas})

@login_required
def IngresarSeleccion(request):
    if request.method=='POST' and request.FILES:
        form=SeleccionForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('selecciones')
    else:
        form=SeleccionForm()
       # contexto={'form':form}
    return render(request,"camisetas/ingresarcamiseta.html",{'form':form})

