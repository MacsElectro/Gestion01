from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
from clientes.models import *
from clientes.forms import empresa_form

def index(request):
    return HttpResponse("Hola mundo")

def registro_empresa(request):
    empresa=Empresa.objects.all()
    return HttpResponse(render(request, 'clientes/index.html', {"empresas":empresa}))

