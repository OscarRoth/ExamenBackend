# Sistema de Gestión de Exámenes

Sistema desarrollado en Django para gestionar profesores, cursadas, exámenes, alumnos y calificaciones.

## Tecnologías

- Python 3.12
- Django
- SQLite
- Git / GitHub

## Modelos principales

- Profesor
- Alumno
- Asignatura
- Cursada
- Inscripcion
- Examen
- AsignacionExamen
- Pregunta
- Respuesta

## Organización del trabajo

El examen estaba pensado para un grupo. En este caso fue realizado de forma individual, dividiendo el trabajo en dos roles:

### Rol 1: Modelado y base de datos

- Diseño de modelos.
- Relaciones.
- Migraciones.
- Normalización en 3FN.

### Rol 2: Administración, consultas y documentación

- Configuración del Admin.
- Carga de datos de prueba.
- Consultas con ORM.
- Documentación del proceso.

## Consultas implementadas

Las consultas están en:

```text
examenes/consultas.py