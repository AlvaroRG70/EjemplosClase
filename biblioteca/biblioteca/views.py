from django.shortcuts import render
from biblioteca.models import Libro, Cliente, Biblioteca
from django.db.models import Q

# Create your views here.

def index(request):
    return render(request, "index.html")

def listar_libros(request):
    libros = Libro.objects.select_related("bliblioteca").prefetch_related("autores")
    return render(request, "libro/lista.html", {"libros_mostrar":libros})

def dame_libros_fecha(request, anyo_libro, mes_libro):
    libros = Libro.objects.select_related("bliblioteca").prefetch_related("autores")
    libros = libros.filter(fecha_publicacion__year = anyo_libro, fecha_publicacion__month = mes_libro)
    return render(request, "libro/lista.html", {"libros_mostrar":libros})

def dame_libros_idioma(request, idioma):
    libros = Libro.objects.select_related("bliblioteca").prefetch_related("autores")
    libros = libros.filter(Q(idioma=idioma)|Q(idioma="ES")).order_by("fecha_publicacion")
    return render(request, "libro/lista.html", {"libros_mostrar":libros})

def dame_libro(request, id_libro):
    libro = Libro.objects.select_related("bliblioteca").prefetch_related("autores").get(id=id_libro)
    return render(request, "libro/libro.html",{"libro":libro})



def listar_clientes(request):
    clientes = Cliente.objects.all()
    return render(request, "cliente/clientelist.html", {"clientes_mostrar":clientes})

def listar_biblioteca(request):
    bibliotecas = Biblioteca.objects.all()
    return render(request, "biblioteca/bibliotecalist.html", {"biblioteca_mostrar":bibliotecas})

