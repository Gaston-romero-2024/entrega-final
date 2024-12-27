from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.views import LoginView
from users.forms import CustomUserCreationForm, Mensajeform
from django.contrib.auth import logout
 # Create your views here.


def inicio(request):

    return render(request,"inicio.html")

class UserLoginView(LoginView):
    template_name='users/login.html'

def CrearU(request):
    if request.method =='post':
        form=CustomUserCreationForm(request.post)
        if form.is_valid():
            form.save()
            return render(request,"users/login.html")
    else:
        form=CustomUserCreationForm()
        return render(request,"users/create.html",{'form':form})
    
def enviar_msj(request):
    if request.method =='POST':
        form=Mensajeform(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Mensaje enviado")
    else:
        form=Mensajeform()
    return render (request,"users/mensaje.html", {"form":form})

def about(request):
    return render(request,'users/about.html')


def logout_view(request):
    logout(request)
    return redirect('login')
   
