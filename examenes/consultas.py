from examenes.models import Examen

examenes_profesor = Examen.objects.filter(
    cursada__profesor__apellido="Perez"
)

for examen in examenes_profesor:
    print(examen.titulo)