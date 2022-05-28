from clientes.views import *
from django.urls import path 

urlpatterns = [
    #path("hola-mundo/", index, name="hola-mundo" ),
    path("registro/", registro_empresa, name="registro_empresa"),
]