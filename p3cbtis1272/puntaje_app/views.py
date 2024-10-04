from django.shortcuts import render

# Create your views here.

def Producto(request):
    return render(request, 'Producto.html')

def Sucursales(request):
    return render(request, 'Sucursales.html') 

def Empleado(request):
    return render(request, 'Empleado.html') 

def Cliente(request):
    return render(request, 'Cliente.html')
