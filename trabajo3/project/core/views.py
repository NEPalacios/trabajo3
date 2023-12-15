from django.shortcuts import render, redirect
from .models import Producto
from django.contrib import messages


# Create your views here.
def index(request):
    return render(request, 'core/index.html')

def consultar(request): 
    productos = Producto.objects.all()
    return render(request, 'core/consultar.html', {
        'productos': productos
        })

def producto(request):
    productos = Producto.objects.all()
    return render(request, 'core/producto.html', {
        'productos': productos
        })


def guardar(request):
    #name en producto.html
    nombre = request.POST['nombre']
    precio = request.POST['precio']
    descripcion = request.POST['descripcion']
   #nueva variable = Modelo(izquierda, nombre en models.variable a la que hacemos referencia)
    p = Producto(nombre=nombre, precio=precio, descripcion=descripcion)
    #guardar datos
    p.save()
    messages.success(request, 'Producto guardado correctamente')
     #redireccionar a otra pagina
    return redirect('core:consultar')

def eliminar(request, id):
    p = Producto.objects.filter(pk=id)
    p.delete()
    messages.success(request, 'Producto eliminado correctamente')
    return redirect('core:consultar')

def detalle(request, id):
    producto = Producto.objects.get(pk=id)
    return render(request, 'core/productoEditar.html', {
        'producto' : producto
    })

def editar(request, id):
    nombre = request.POST['nombre']
    precio = request.POST['precio']
    descripcion = request.POST['descripcion']
    id = request.POST['id']
    Producto.objects.filter(pk=id).update(id=id, nombre=nombre,
                                               precio=precio,
                                                 descripcion=descripcion)
    messages.success(request, 'Producto actualizado correctamente')
    return redirect('core:consultar')

def buscar(request):
   pass