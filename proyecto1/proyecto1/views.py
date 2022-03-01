from django.http import HttpResponse
import datetime
from django.template import Context, Template
from django.shortcuts import render



class Persona(object):
    def __init__(self,nombre2,apellido2):
        self.nombre2=nombre2
        self.apellido2=apellido2


def saludo(request):

    PERSONA = Persona("silfredo","OROZCO")

    #nombre="Juan"

    #apellido="Diaz"

    temascurso=["plantillas","modelos","formularios","vistas","despliegue"]

    fecha_actual=datetime.datetime.now()
    
    #documento_externo=open('C:/Users/PC/Documents/ProyectoPython/proyecto1/proyecto1/plantilla/miPlantilla.html')

    #plt=Template(documento_externo.read())

    #documento_externo.close()
    
    #ctx=Context({"nombre_persona":PERSONA.nombre2,"apellido_persona":PERSONA.apellido2,"hora":fecha_actual,"temas":temascurso})

    #documento=plt.render(ctx)

    return render(request,"miPlantilla.html",{"nombre_persona":PERSONA.nombre2,"apellido_persona":PERSONA.apellido2,"hora":fecha_actual,"temas":temascurso})



def despedida(request):
    return HttpResponse("adios eres el mejor")



def dameFecha(request):
    fecha_actual=datetime.datetime.now()

    documento="""<html>
    <br>
    <center>
    <body>
    <h1>
    Fecha y hora actuales %s
    </h1>
    </body>
    </center>
    </html>"""% fecha_actual
    return HttpResponse(documento)


def calcularEdad(request,edad,ago):
    # edadActual=16
    periodo = ago - 2021
    edadFutura = edad + periodo
    documento="""<html>
    <br>
    <center>
    <body>
    <h1>
    Camilo En el año %s tendras %s años
    </h1>
    </body>
    </center>
    </html>"""% (ago,edadFutura)
    return HttpResponse(documento )



def cursoC(request):
    fecha_actual=datetime.datetime.now()

    return render(request,'cursoC.html',{'fecha':fecha_actual})




def cursoCSS(request):

    fecha_actual=datetime.datetime.now()

    return render(request,'cursoCSS.html',{'fecha':fecha_actual})