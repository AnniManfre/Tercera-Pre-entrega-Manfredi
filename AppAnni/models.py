from django.db import models

class Actor(models.Model):
    nombre = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()

    def __str__(self):
        return self.nombre

class Genero(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Pelicula(models.Model):
    titulo = models.CharField(max_length=200)
    anio = models.PositiveIntegerField()
    genero = models.ForeignKey(Genero, on_delete=models.CASCADE)
    actores = models.ManyToManyField(Actor, related_name='peliculas')

    def __str__(self):
        return self.titulo

