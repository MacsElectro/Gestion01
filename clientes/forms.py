from statistics import mode
from django import forms
#from .models import Empresa 

class empresa_form(forms.Form):
    razon_social=forms.CharField(label="Razon Social", max_length=50)
    direccion=forms.CharField(label="Dirección", max_length=50)
    cuit=forms.CharField(label="CUIT", max_length=11)
    email = forms.EmailField(label="Email")
    telefono=forms.CharField(label="Telefono", max_length=14)
    # input_format hace que se pueda ingresar la fecha con el formato latino, dia/mes/año
    fecha_registro = forms.DateField(label="Fecha Registro", input_formats=["%d/%m/%Y"],
    #widget es para poder agregar un tip para que el usuario sepa como ingresar la fecha
    widget=forms.TextInput(attrs={'placeholder': '30/12/1995'}))
    

