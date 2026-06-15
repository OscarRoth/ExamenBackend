# Registro de consultas realizadas con IA por Norberto Oscar Roth

## Objetivo

Durante el desarrollo de este proyecto utilicé asistencia de IA como herramienta de apoyo para resolver dudas de implementación, organización del proyecto y validación de decisiones de diseño.

Utilicé IA fue como recurso de consulta y acompañamiento técnico. La implementación, las pruebas, la validación de resultados y las decisiones finales fueron realizadas por mí sobre el proyecto desarrollado.

---

## Organización del trabajo

Aunque el examen fue planteado para realizarse en grupo, decidí desarrollarlo de forma individual.

Con el objetivo de mantener una organización similar a la de un entorno colaborativo real y optimizar el desarrollo, dividí el trabajo en dos roles diferenciados.

### Rol 1: Arquitectura y Base de Datos

Responsabilidades:

* Diseño de modelos.
* Definición de relaciones entre entidades.
* Aplicación de criterios de normalización.
* Generación y aplicación de migraciones.
* Validación de la estructura de datos.

### Rol 2: Administración y Consultas

Responsabilidades:

* Configuración del panel de administración de Django.
* Carga de datos de prueba.
* Implementación y validación de consultas ORM.
* Verificación funcional del sistema.
* Documentación y preparación de la entrega.

Esta división me permitió organizar mejor las tareas y mantener una metodología de trabajo similar a la que se utilizaría en un equipo de desarrollo.

---

## 1. Organización del repositorio Git

Consulté sobre la forma correcta de organizar el repositorio y trabajar con ramas para representar los distintos roles definidos durante el desarrollo.

Temas tratados:

* Creación de ramas de trabajo.
* Uso de GitHub para versionar y subir cambios.
* Diferencias entre las ramas `main`, `modelos-bd` y `admin-consultas`.
* Integración de cambios mediante merge.
* Resolución de errores relacionados con commits y pushes.

Resultado:

Se definieron ramas separadas para organizar el trabajo y se mantuvo un historial de commits identificable y coherente.

---

## 2. Diseño de modelos y normalización

Consulté sobre la estructura adecuada para representar profesores, alumnos, asignaturas, cursadas, exámenes y demás entidades requeridas por la consigna.

Durante el análisis surgió la necesidad de modelar correctamente la relación entre alumnos y cursadas. Para evitar redundancia de información y cumplir con los criterios de tercera forma normal (3FN), decidí implementar una tabla intermedia denominada `Inscripcion`.

Esta entidad permite representar la relación muchos a muchos entre alumnos y cursadas sin duplicar datos, manteniendo cada concepto en su propia tabla y evitando dependencias transitivas.

Resultado:

* Modelos normalizados en tercera forma normal (3FN).
* Separación clara de responsabilidades entre entidades.
* Implementación de la tabla intermedia `Inscripcion`.
* Reducción de redundancia y mejora de la integridad de los datos.

---

## 3. Migraciones y administración

Consulté sobre los pasos necesarios para:

* Crear migraciones.
* Aplicarlas correctamente.
* Registrar modelos en Django Admin.
* Crear un superusuario.
* Verificar el funcionamiento del panel administrativo.

Resultado:

Se logró administrar correctamente todas las entidades desde el panel de administración de Django.

---

## 4. Carga y validación de datos

Consulté sobre la forma adecuada de cargar datos de prueba y verificar que las relaciones entre entidades funcionaran correctamente.

Temas tratados:

* Creación de profesores.
* Creación de alumnos.
* Creación de asignaturas.
* Creación de cursadas.
* Creación de exámenes.
* Asignación de exámenes a alumnos.
* Validación de relaciones entre modelos.

Resultado:

Se verificó correctamente la consistencia de los datos mediante el panel administrativo.

---

## 5. Consultas ORM

Consulté sobre la construcción y validación de consultas utilizando el ORM de Django.

Las consultas implementadas fueron:

1. Obtener todos los exámenes creados por un profesor.
2. Obtener los exámenes asignados a un alumno junto con su calificación.
3. Obtener los alumnos que aún no han resuelto los exámenes asignados.

Resultado:

Las consultas fueron verificadas mediante `python manage.py shell` y contrastadas con los datos cargados desde el panel administrativo.

---

## 6. Documentación y estructura final

Consulté sobre:

* Creación y organización del archivo README.
* Generación del archivo `requirements.txt`.
* Organización final del repositorio.
* Revisión de la estructura de entrega.

Resultado:

Se completó la documentación necesaria para facilitar la instalación, comprensión y revisión del proyecto.

---


