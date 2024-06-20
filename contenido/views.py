from django.shortcuts import render

# Create your views here.

def principal(request):
    return render(request,"contenido/principal.html")

def cursos(request):
    return render(request,"contenido/curso.html")

def contacto(request):
    return render(request,"contenido/contacto.html")

def test(request):
    return render(request,"contenido/ejemplo.html")