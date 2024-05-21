from django import forms
from .models import DepartamentosDef

class DepartamentosDefForm (forms.ModelForm):
    class Meta:
        model=DepartamentosDef
        fields="__all__"