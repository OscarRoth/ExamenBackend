# Registro de consultas realizadas con IA

## Objetivo

Durante el desarrollo del proyecto se utilizó asistencia de IA como apoyo para resolver dudas de implementación, organización del proyecto y validación de decisiones de diseño.

La IA fue utilizada como herramienta de consulta y acompañamiento técnico, mientras que la implementación, pruebas y verificación final fueron realizadas manualmente sobre el proyecto.

---

## Consulta 1: Organización del repositorio Git

Se consultó sobre la forma correcta de trabajar con ramas para representar los distintos roles del examen.

Temas tratados:

* Creación de ramas de trabajo.
* Uso de GitHub para subir cambios.
* Diferencias entre `main`, `modelos-bd` y `admin-consultas`.
* Integración de ramas mediante merge.
* Resolución de errores al intentar realizar commits y pushes.

Resultado:

Se definieron ramas separadas para representar los distintos roles y se mantuvo un historial de commits identificable.

---

## Consulta 2: Diseño de modelos y normalización

Se consultó sobre la estructura adecuada para representar:

* Profesores.
* Alumnos.
* Asignaturas.
* Cursadas.
* Exámenes.
* Preguntas.
* Respuestas.

También se analizó la conveniencia de utilizar tablas intermedias para relaciones muchos a muchos.

Resultado:

Se implementó la entidad `Inscripcion` para representar la relación entre alumnos y cursadas, aplicando criterios de tercera forma normal (3FN) y evitando redundancia de datos.

---

## Consulta 3: Migraciones y administración

Se solicitaron indicaciones para:

* Crear migraciones.
* Aplicarlas correctamente.
* Registrar modelos en Django Admin.
* Crear un superusuario.
* Verificar el funcionamiento del panel administrativo.

Resultado:

Se logró administrar todas las entidades desde el panel de Django.

---

## Consulta 4: Carga y validación de datos

Se consultó sobre la forma de ingresar datos de prueba y validar las relaciones entre entidades.

Temas tratados:

* Creación de profesores.
* Creación de alumnos.
* Asignación de cursadas.
* Creación de exámenes.
* Asignación de exámenes a alumnos.

Resultado:

Se verificó correctamente la consistencia de los datos mediante el panel administrativo.

---

## Consulta 5: Consultas ORM

Se solicitó ayuda para construir y verificar consultas utilizando el ORM de Django.

Consultas implementadas:

1. Obtener los exámenes creados por un profesor.
2. Obtener los exámenes asignados a un alumno junto con su calificación.
3. Obtener los alumnos con exámenes pendientes de resolución.

Resultado:

Las consultas fueron probadas utilizando `python manage.py shell` y devolvieron los resultados esperados.

---

## Consulta 6: Documentación y estructura final

Se consultó sobre:

* Creación de README.
* Generación de requirements.txt.
* Organización final del repositorio.
* Revisión de la estructura de entrega.

Resultado:

Se completó la documentación necesaria para facilitar la instalación y revisión del proyecto.

---

## Conclusión

La asistencia de IA fue utilizada como herramienta de apoyo técnico durante el desarrollo. Su principal aporte consistió en aclarar dudas sobre Django, Git, diseño de modelos y consultas ORM. Todas las decisiones finales, pruebas y verificaciones fueron realizadas sobre el proyecto implementado.
