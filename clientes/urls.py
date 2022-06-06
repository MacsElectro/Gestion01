from turtle import home
from clientes.views import *
from django.urls import path 

urlpatterns = [
    path("", home, name="Home" ),
    path("registro/", registro, name="Registro"),
    path("clientes/", clientes, name="Clientes"),
    path("presupuestos/", presupuestos, name="Presupuestos"),
    path("contacto/", contacto, name="Contacto"),
    path("editar_empresa/<id>/", edit_empresa, name="Edit_emp"),
    path("eliminar_empresa/<id>/", eliminar_empresa, name="Eliminar_emp"),
]