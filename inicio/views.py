from django.shortcuts import render

# Create your views here.

def principal(request):
    return render(request,"inicio/principal.html")

def cursos(request):
    return render(request,"inicio/curso.html")

def contacto(request):
    return render(request,"inicio/contacto.html")

def test(request):
    return render(request,"inicio/ejemplo.html")