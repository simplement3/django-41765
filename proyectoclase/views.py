from datetime import datetime
import random
from django.http import HttpResponse
from django.template import Context, Template, loader

from home.models import persona


def hola(request):
    return HttpResponse("<h1>buenas clase 41765!</h1>")

def fecha(request):
    fecha_y_hora = datetime.now()
    return HttpResponse(f"la fecha y hora actual es: {fecha_y_hora}")

def calcular_fecha_nacimiento(request, edad):
    fecha = datetime.now().year - edad 
    return HttpResponse(f"tu fecha de nacimiento aproxiamda para tus {edad} años seria {fecha}")

def mi_template(request):
    cargar_archivo = open(r"C:\Users\ignac\Documents\projectMVT\templates\mi_template.html", "r")
    template = Template(cargar_archivo.read())
    cargar_archivo.close()
    contexto = Context() 
    template_renderizado = template.render(contexto)
    return HttpResponse(template_renderizado)

def tu_template(request, nombre):
    template = loader.get_template("tu_template.html")
    template_renderizado = template.render({"persona" : nombre})
    return HttpResponse(template_renderizado)

def prueba_template(request):

    mi_contexto = {
        "rango": list(range(1,11)),
        "valor_aleatorio": random.randrange(1,11)
    }
    
    template = loader.get_template("prueba_template.html")
    template_renderizado = template.render(mi_contexto)
    
    return HttpResponse(template_renderizado)

def crear_persona(resquest):
    return HttpResponse("")

def ver_personas(resquest):
    personas = persona.objects.all()

    template = loader.get_template("ver_personas.html")
    template_renderizado = template.render({"personas": personas})
    return HttpResponse(template_renderizado)