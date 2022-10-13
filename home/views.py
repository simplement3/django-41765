from datetime import datetime
import random
from urllib import request
from django.http import HttpResponse
from django.template import Context, Template, loader
from home.models import Humano
from django.shortcuts import render


def hola(request):
    return HttpResponse('<h1>buenas clase 41765!</h1><a class="navbar-brand" href={% url "Home" %} >Home</a>')

def fecha(request):
    fecha_y_hora = datetime.now()
    return HttpResponse(f"la fecha y hora actual es: {fecha_y_hora}")

def calcular_fecha_nacimiento(request, edad):
    fecha = datetime.now().year - edad 
    return HttpResponse(f"tu fecha de nacimiento aproxiamda para tus {edad} años seria {fecha}")

def mi_template(request):
    cargar_archivo = open(r"C:\Users\ignac\Documents\projectMVT\home\templates\mi_template.html", "r")
    template = Template(cargar_archivo.read())
    cargar_archivo.close()
    contexto = Context() 
    template_renderizado = template.render(contexto)
    return HttpResponse(template_renderizado)

def tu_template(request, nombre):
    template = loader.get_template("home/tu_template.html")
    template_renderizado = template.render({"persona" : nombre})
    return HttpResponse(template_renderizado)

def prueba_template(request):

    mi_contexto = {
        "rango": list(range(1,11)),
        "valor_aleatorio": random.randrange(1,11)
    }
    
    template = loader.get_template("home/prueba_template.html")
    template_renderizado = template.render(mi_contexto)
    
    return HttpResponse(template_renderizado)
    
def crear_persona(request):
   
    # persone =  Humano(nombre=nombre, apellido=apellido, edad=random.randrange(1,99), fecha_nacimiento=datetime.now())     
    # persone.save()


    return render(request, 'home/crear_persona.html', {})

def ver_personas(request):
    
    personas = Humano.objects.all()

    # template = loader.get_template("ver_personas.html")
    # template_renderizado = template.render({"personas": personas})
    
    # return HttpResponse(template_renderizado) 
    return render(request, 'home/ver_personas.html', {'personas': personas})

def index(request):
   
    return render(request,'home/index.html')