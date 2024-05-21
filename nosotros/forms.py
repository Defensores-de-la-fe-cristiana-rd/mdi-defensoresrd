from django import forms
from .models import NosotrosDef, Imagen, Archivo


class NosotrosDefForm (forms.ModelForm):
    class Meta:
        model=NosotrosDef
        fields="__all__"

class ImagenForm(forms.ModelForm):
    class Meta:
        model = Imagen
        fields="__all__"

        
class ArchivoForm(forms.ModelForm):
    class Meta:
        model = Archivo
        fields="__all__"

