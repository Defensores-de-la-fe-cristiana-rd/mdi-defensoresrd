from django import forms
from .models import PresbiteriosDef

class PresbiteriosDefForm (forms.ModelForm):
    class Meta:
        model=PresbiteriosDef
        fields="__all__"