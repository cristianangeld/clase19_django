from django.db import models
from django.forms import BooleanField
class Curso(models.Model):
    nombre = models.CharField(max_length=64)
    comision = models.IntegerField()

class Estudiante(models.Model):
    apellido = models.CharField(max_length=256)
    nombre = models.CharField(max_length=256)
    email = models.EmailField()
    telefono = models.CharField(max_length=20)
    dni = models.CharField(max_length=32)
    fecha_nacimiento = models.DateField()

class Profesor(models.Model):
    apellido = models.CharField(max_length=256)
    nombre = models.CharField(max_length=256)
    email = models.EmailField()
    profesion = models.CharField(max_length=128)
    dni = models.CharField(max_length=32)
    fecha_nacimiento = models.DateField()
    bio = models.TextField()

class Entregable(models.Model):
    nombre = models.CharField(max_length=256)
    fecha_entrega = models.DateTimeField()
    esta_aprobado = models.BooleanField(default=False)



