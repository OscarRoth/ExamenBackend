from examenes.models import Examen, AsignacionExamen


# Consulta 1: todos los exámenes creados por un profesor
examenes_profesor = Examen.objects.filter(
    cursada__profesor__apellido="Perez"
)

for examen in examenes_profesor:
    print(examen.titulo)


# Consulta 2: exámenes asignados a un alumno y su calificación
asignaciones = AsignacionExamen.objects.filter(
    alumno__apellido="Lopez"
)

for asignacion in asignaciones:
    print(
        asignacion.examen.titulo,
        asignacion.calificacion
    )


# Consulta 3: alumnos que aún no resolvieron exámenes asignados
pendientes = AsignacionExamen.objects.filter(
    fecha_resolucion__isnull=True
)

for pendiente in pendientes:
    print(
        pendiente.alumno,
        pendiente.examen
    )