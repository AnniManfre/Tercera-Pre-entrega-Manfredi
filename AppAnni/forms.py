from django import forms
from .models import Actor, Pelicula, Genero

class ActorForm(forms.ModelForm):
    class Meta:
        model = Actor
        fields = ['nombre', 'fecha_nacimiento']

class GeneroForm(forms.ModelForm):
    class Meta:
        model = Genero
        fields = ['nombre']

class PeliculaForm(forms.ModelForm):
    class Meta:
        model = Pelicula
        fields = ['titulo', 'anio', 'genero', 'actores']
