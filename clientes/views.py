from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.http import HttpResponse
#from django.urls import is_valid_path
from .forms import *
from .models import *


def home(request):
    return HttpResponse(render(request, 'clientes/home.html'))




def registro(request):

    formulario_regi=empresa_form()

    if request.method=="POST":
        formulario_regi=empresa_form(request.POST)
        

        if formulario_regi.is_valid():
            form_data=formulario_regi.cleaned_data
            razon = form_data.get("razon_social")
            dire = form_data.get('direccion')
            cuit = form_data.get('cuit')
            ema = form_data.get('email')
            telef = form_data.get('telefono')
            fecha_Reg = form_data.get('fecha_registro')
            Empresa(razon_social=razon, direccion=dire, cuit=cuit, email=ema, telefono=telef, fecha_registro=fecha_Reg).save()
            return render(request, 'clientes/registro.html',{'formu_reg':empresa_form})
        else:
            #import pdb; pdb.set_trace()
            return render(request, 'clientes/registro.html',{'formu_reg':formulario_regi})





    return HttpResponse(render(request, 'clientes/registro.html',{'formu_reg':formulario_regi}))

def clientes(request):
    empresa=Empresa.objects.all()

    return HttpResponse(render(request, 'clientes/clientes.html', {"empresa":empresa})) 
    #import pdb; pdb.set_trace()


def edit_empresa(request, id):
    data=Empresa.objects.get(id=id)
    itens_Id= {'formu_reg':edit_form(instance=data)}

    if request.method == 'POST':
        
        formulario=edit_form(data=request.POST, instance=data)
        
        if formulario.is_valid():
            formulario.save()
            itens_Id={'formu_reg':edit_form()}

            itens_Id['mensaje']="Se Actualizo Correctamente"
        else:

            return render(request, 'clientes/registro.html', {'formu_reg':formulario})

    return render(request, 'clientes/editar_empresa.html', itens_Id)

def eliminar_empresa(request, id):
    data=Empresa.objects.get(id=id)
    data.delete()

    return redirect(to="Clientes")


def presupuestos(request):
    return HttpResponse(render(request, 'clientes/presupuestos.html'))  

def contacto(request):
    return HttpResponse(render(request, 'clientes/contacto.html'))       



