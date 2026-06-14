from django.contrib import admin

from .models import (
    Alumno,
    AsignacionExamen,
    Asignatura,
    Cursada,
    Examen,
    Inscripcion,
    Pregunta,
    Profesor,
    Respuesta,
)


admin.site.register(Profesor)
admin.site.register(Alumno)
admin.site.register(Asignatura)
admin.site.register(Cursada)
admin.site.register(Inscripcion)
admin.site.register(Examen)
admin.site.register(AsignacionExamen)
admin.site.register(Pregunta)
admin.site.register(Respuesta)