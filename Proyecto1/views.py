from django.http import HttpResponse
import datetime

def saludo(request):
    
    return HttpResponse("Hola alumnos esta es nuestra primera página con Django") 

def despedida(request):
    
    return HttpResponse("Hasta luego alumnos de Django") 

def dameFecha(request):
    
    fecha_actual = datetime.datetime.now()
    
    documento ="""
    <html>
    <body>
    <h2>
    Fecha y hora actuales %s
    </h2>
    </body>
    </html> """ % fecha_actual
    
    return HttpResponse(documento) 

def calculaEdad(request,edad,agno):
    
    periodo = agno - 2023
    edadFutura = edad+ periodo
    documento = """
    <html>
    <body>
    <h2>
    En el año %s tendrás %s años 
    </h2>
    </body>
    </html> 
    """ %(agno,edadFutura)
    
    return HttpResponse(documento)