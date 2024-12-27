from django import forms
from camisetas.models import Seleccion

class SeleccionForm(forms.ModelForm):
    class Meta:
        model=Seleccion
        fields=["pais","fecha","titular","imagen"]

