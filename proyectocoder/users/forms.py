
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm,UserCreationForm,AuthenticationForm
from .models import Mensaje
from django import forms

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model=User
        fields=("username","password1","password2","email","first_name","last_name")

class CustomUserChangeForm(UserChangeForm):
    password=None
    class Meta:
        fields=fields=("username","email","first_name","last_name")

class Mensajeform(forms.ModelForm):
    class Meta:
        model=Mensaje
        fields=["nombre","email","asunto","mensajes"]
        widgets = {
            'mensaje': forms.Textarea(attrs={'rows': 5, 'cols': 40}),
        }