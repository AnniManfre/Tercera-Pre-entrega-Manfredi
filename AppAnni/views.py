from django.shortcuts import render, redirect
from .forms import ActorForm, GeneroForm, PeliculaForm
from .models import Pelicula

def inicio(request):
    return render(request, 'AppAnni/inicio.html')

def agregar_actor(request):
    if request.method == 'POST':
        form = ActorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inicio')
    else:
        form = ActorForm()
    return render(request, 'AppAnni/agregar_actor.html', {'form': form})

def agregar_genero(request):
    if request.method == 'POST':
        form = GeneroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inicio')
    else:
        form = GeneroForm()
    return render(request, 'AppAnni/agregar_genero.html', {'form': form})

def agregar_pelicula(request):
    if request.method == 'POST':
        form = PeliculaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inicio')
    else:
        form = PeliculaForm()
    return render(request, 'AppAnni/agregar_pelicula.html', {'form': form})

def buscar_pelicula(request):
    if request.method == 'GET':
        query = request.GET.get('query')
        if query:
            resultados = Pelicula.objects.filter(titulo__icontains=query)
            return render(request, 'AppAnni/resultados_busqueda.html', {'resultados': resultados})
    return render(request, 'AppAnni/buscar_pelicula.html')
