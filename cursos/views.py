from django.shortcuts import render
from .models import Cursos

# Create your views here.

def cursos(request):
    cursos=Cursos.objects.all()
    return render(request, "cursos/curso.html", {"cursos":cursos})


def consultar1(request):
    cursos = Cursos.objects.filter(categoria="informatica")
    return render(request, 'cursos/consultas.html', {'cursos': cursos})
def consultar2(request):
    cursos = Cursos.objects.filter(categoria="informatica").filter(nombre="Python")
    return render(request, 'cursos/consultas.html', {'cursos': cursos})
def consultar3(request):
    cursos = Cursos.objects.filter(precio__gt=150)
    return render(request, 'cursos/consultas.html', {'cursos': cursos})
def consultar4(request):
    cursos = Cursos.objects.filter(actividad__desc__contains="REalizar app")
    return render(request, 'cursos/consultas.html', {'cursos': cursos})


###################### Seguridad
def formMateria(request, nombre=None, carrera=None, profesor=None):
    nombre = request.GET.get('nombre')
    carrera = request.GET.get('carrera')
    profesor = request.GET.get('profesor')
    return render(request, 'cursos/form_materia.html', {'nombre': nombre, 'carrera': carrera, 'profesor': profesor})
    