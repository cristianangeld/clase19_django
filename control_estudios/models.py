from django.db import models
from django.forms import BooleanField

class Curso(models.Model):
    nombre = models.CharField(max_length=64)  
    comision = models.IntegerField()  

    def __str__(self):
        return f"{self.nombre} | {self.comision}"


class Estudiante(models.Model):
    apellido = models.CharField(max_length=256)
    nombre = models.CharField(max_length=256)
    email = models.EmailField(blank=True)
    telefono = models.CharField(max_length=20, blank=True)
    dni = models.CharField(max_length=32)
    cursos = models.ManyToManyField(Curso)  

    def __str__(self):
        return f"{self.nombre}, {self.apellido}"


class Profesor(models.Model):
    apellido = models.CharField(max_length=256)
    nombre = models.CharField(max_length=256)
    dni = models.CharField(max_length=32)
    email = models.EmailField(blank=True)
    fecha_nacimiento = models.DateField(null=True, blank=True)
    profesion = models.CharField(max_length=128)
    bio = models.TextField(blank=True)

    def __str__(self):
        return f"{self.nombre}, {self.apellido}"


class Entregable(models.Model):
    nombre = models.CharField(max_length=256)
    fecha_entrega = models.DateTimeField(auto_now_add=True)
    esta_aprobado = models.BooleanField(default=False)  # equivalente a bool (True, False)



