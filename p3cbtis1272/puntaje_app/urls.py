from django.urls import path
from . import views
urlpatterns = [
    path("",views.Producto,name="Producto"),
    path("Sucursales/",views.Sucursales,name="Sucursales"),
    path("Empleado/",views.Empleado,name="Empleado"), 
    path("Cliente/",views.Cliente,name="Cliente")
]
