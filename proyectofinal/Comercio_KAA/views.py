from django.db.models.query import QuerySet
from django.db.models import Q
from django.shortcuts import render, HttpResponse

from django.shortcuts import get_object_or_404

from .models import Producto, Categoria

# Create your views here.

def home(request):    
    productos=Producto.objects.all() 
    categorias=Categoria.objects.all()
    productostres=Producto.objects.order_by('-precio') [:3]
    productosres=Producto.objects.order_by('-precio') [3:10]
    
    context={'categorias':categorias,'productostres':productostres,
        'productosres':productosres,'productos':productos}

    return render(request, "Comercio_KAA/home.html", context)

def acerca_de(request):
    productos=Producto.objects.all()
    categorias=Categoria.objects.all()

    context={'categorias':categorias,'productos':productos}
    
    return render(request, "Comercio_KAA/acerca_de.html", context)

def producto(request,slug):

    productos=Producto.objects.all()
    categorias=Categoria.objects.all()
    productodet=Producto.objects.get(slug=slug)
    
    context= {'categorias':categorias,'productos':productos,'productodet':productodet}

    return render(request, "Comercio_KAA/producto.html", context)

def categoria(request,slug):
    productos=Producto.objects.all()
    categorias=Categoria.objects.all()
    categoriadet=Categoria.objects.get(slug=slug)
    cereales=Producto.objects.filter(categoria__in=[2])
    especias=Producto.objects.filter(categoria__in=[3])
    frutos_secos=Producto.objects.filter(categoria__in=[4])
    
    
    context= {'categorias':categorias,'productos':productos,'categoriadet':categoriadet,
        'cereales':cereales,'especias':especias,'frutos_secos':frutos_secos}

    return render(request, "Comercio_KAA/categoria.html", context)

def busqueda_cat(request):
    queryset=request.GET.get("buscar")
    productos=Producto.objects.all()
    categorias=Categoria.objects.all()
    cereales=Producto.objects.filter(categoria__in=[2])
    especias=Producto.objects.filter(categoria__in=[3])
    frutos_secos=Producto.objects.filter(categoria__in=[4])

    if queryset:
        productos=Producto.objects.filter(Q(categoria__titulo__icontains= queryset)).distinct()

    context= {'categorias':categorias,'productos':productos,'cereales':cereales,
        'especias':especias,'frutos_secos':frutos_secos,'queryset':queryset}

    return render(request, "Comercio_KAA/busqueda.html",context)

