from django.http import HttpResponse

def saludo(request):
    
    return HttpResponse("Hola alumnos esta es nuestra primera página con Django") 

def despedida(request):
    
    return HttpResponse("Hasta luego alumnos de Django") 
#This is a comment