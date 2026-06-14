from django.db import models


class Profesor(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"
    
    class Meta:
        verbose_name = "Profesor"
        verbose_name_plural = "Profesores"

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
        verbose_name = "Inscripción"
        verbose_name_plural = "Inscripciones"

    def __str__(self):
        return f"{self.alumno} - {self.cursada}"
    
class Examen(models.Model):
    titulo = models.CharField(max_length=150)
    fecha_creacion = models.DateField(auto_now_add=True)
    cursada = models.ForeignKey(
        Cursada,
        on_delete=models.CASCADE,
        related_name='examenes'
    )

    def __str__(self):
        return self.titulo
    
    class Meta:
        verbose_name = "Exámen"
        verbose_name_plural = "Examenes"


class AsignacionExamen(models.Model):
    examen = models.ForeignKey(
        Examen,
        on_delete=models.CASCADE,
        related_name='asignaciones'
    )
    alumno = models.ForeignKey(
        Alumno,
        on_delete=models.CASCADE,
        related_name='asignaciones_examenes'
    )
    fecha_asignacion = models.DateField(auto_now_add=True)
    fecha_resolucion = models.DateField(
        null=True,
        blank=True
    )
    calificacion = models.DecimalField(
        max_digits=4,
        decimal_places=2,
        null=True,
        blank=True
    )
    observaciones = models.TextField(
        blank=True
    )

    class Meta:
        unique_together = ('examen', 'alumno')
        verbose_name = "Asignación Exámen"
        verbose_name_plural = "Asignacion Examenes"

    def __str__(self):
        return f"{self.examen} - {self.alumno}"


class Pregunta(models.Model):
    examen = models.ForeignKey(
        Examen,
        on_delete=models.CASCADE,
        related_name='preguntas'
    )
    fecha_creacion = models.DateField(auto_now_add=True)
    titulo = models.CharField(max_length=150)
    descripcion = models.TextField()

    def __str__(self):
        return self.titulo


class Respuesta(models.Model):
    pregunta = models.ForeignKey(
        Pregunta,
        on_delete=models.CASCADE,
        related_name='respuestas'
    )
    texto = models.TextField()
    es_correcta = models.BooleanField(default=False)

    def __str__(self):
        return self.texto[:50]