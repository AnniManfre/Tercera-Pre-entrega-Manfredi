
from django.urls import path
from .views import agregar_actor, agregar_genero, agregar_pelicula, buscar_pelicula, inicio

urlpatterns = [
    path('agregar-actor/', agregar_actor, name='agregar_actor'),
    path('agregar-genero/', agregar_genero, name='agregar_genero'),
    path('agregar-pelicula/', agregar_pelicula, name='agregar_pelicula'),
    path('buscar-pelicula/', buscar_pelicula, name='buscar_pelicula'),
    path('', inicio, name='inicio'),  # Suponiendo que tienes una vista de inicio
]
