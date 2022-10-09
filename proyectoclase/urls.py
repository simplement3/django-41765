"""proyectoclase URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from cgitb import html
from . import views
from django.contrib import admin
from django.urls import path
# from .views import hola

urlpatterns = [
    path('admin/', admin.site.urls),
    path('fecha/', views.fecha),
    path('fecha-nacimiento/<int:edad>/', views.calcular_fecha_nacimiento),
    # path('hola/', hola),
    # path('fecha/', fecha),
    path('hola/', views.hola),
    path('mi-template/', views.mi_template),
    path('mi-template/<str:nombre>/', views.tu_template),
    path('prueba-template/', views.prueba_template),
    path('ver-personas/', views.ver_personas),
    # path('crear-persona/<str:nombre>/<str:apellido>/', views.crear_persona),
    path('crear-persona/', views.crear_persona)
]  
