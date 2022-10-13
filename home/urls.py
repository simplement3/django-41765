
from django.urls import path
# from .views import hola
from home import views

urlpatterns = [
    path('', views.index, name='Home'),
    path('fecha/', views.fecha, name= 'Fecha'),
    path('fecha-nacimiento/<int:edad>/', views.calcular_fecha_nacimiento),
    # path('hola/', hola),
    # path('fecha/', fecha),
    path('hola/', views.hola, name='Hola'),
    # path('mi-template/', views.mi_template, name='mi_template'),
    path('mi-template/<str:nombre>/', views.tu_template),
    path('prueba-template/', views.prueba_template),
    path('ver-personas/', views.ver_personas, name='ver_personas'),
    # path('crear-persona/<str:nombre>/<str:apellido>/', views.crear_persona),
    path('crear-persona/', views.crear_persona, name='crear_persona')
    ]
    
