from django.db import models


class Profesor(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class Alumno(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    numero_identificacion = models.CharField(
        max_length=20,
        unique=True
    )

    def __str__(self):
        return f"{self.nombre} {self.apellido}"


class Asignatura(models.Model):
    nombre = models.CharField(max_length=100)
    codigo = models.CharField(
        max_length=20,
        unique=True
    )
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre
