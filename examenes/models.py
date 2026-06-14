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

class Cursada(models.Model):
    ESTADO_ACTIVA = 'activa'
    ESTADO_FINALIZADA = 'finalizada'

    ESTADOS = [
        (ESTADO_ACTIVA, 'Activa'),
        (ESTADO_FINALIZADA, 'Finalizada'),
    ]

    nombre = models.CharField(max_length=100)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    estado = models.CharField(
        max_length=20,
        choices=ESTADOS,
        default=ESTADO_ACTIVA
    )
    profesor = models.ForeignKey(
        Profesor,
        on_delete=models.CASCADE,
        related_name='cursadas'
    )
    asignatura = models.ForeignKey(
        Asignatura,
        on_delete=models.CASCADE,
        related_name='cursadas'
    )
    alumnos = models.ManyToManyField(
        Alumno,
        through='Inscripcion',
        related_name='cursadas'
    )

    def __str__(self):
        return self.nombre


class Inscripcion(models.Model):
    alumno = models.ForeignKey(
        Alumno,
        on_delete=models.CASCADE,
        related_name='inscripciones'
    )
    cursada = models.ForeignKey(
        Cursada,
        on_delete=models.CASCADE,
        related_name='inscripciones'
    )
    fecha_inscripcion = models.DateField(auto_now_add=True)

    class Meta:
        unique_together = ('alumno', 'cursada')

    def __str__(self):
        return f"{self.alumno} - {self.cursada}"