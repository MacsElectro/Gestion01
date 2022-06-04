from turtle import home
from clientes.views import *
from django.urls import path 

urlpatterns = [
    path("", home, name="Home" ),
    path("registro/", registro, name="Registro"),
    path("clientes/", clientes, name="Clientes"),
    path("presupuestos/", presupuestos, name="Presupuestos"),
    path("contacto/", contacto, name="Contacto"),

]