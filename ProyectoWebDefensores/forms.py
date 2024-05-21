from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Post, Noticias, Contactanos, Comentario, ImagenCarrusel





class CustomUserCreationForm(UserCreationForm):
    
    class Meta:
        model = User
        fields=['username', 'first_name', 'last_name', 'email', 'password1', 'password2']

class PostForm (forms.ModelForm):
    class Meta:
        model=Post
        fields=['titulo', 'contenido', 'imagen']

class NoticiasForm (forms.ModelForm):
    class Meta:
        model=Noticias
        fields=['tituloPequeno', 'tituloGrande', 'contenidoPequeno', 'contenido', 'imagen']


class ContactanosForm (forms.ModelForm):
    class Meta:
        model=Contactanos
        fields="__all__"

class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields="__all__"

class CarruselForm(forms.ModelForm):
    class Meta:
        model = ImagenCarrusel
        fields="__all__"