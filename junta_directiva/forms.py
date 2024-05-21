from django import forms
from .models import junta_directiva

class DirectivaForm (forms.ModelForm):
    class Meta:
        model=junta_directiva
        fields="__all__"

