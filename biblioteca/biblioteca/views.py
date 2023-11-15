from django.shortcuts import render, redirect
from biblioteca.models import Libro, Cliente, Biblioteca
from django.db.models import Q
from django.views.defaults import page_not_found
from .forms import LibroForms, LibroModelForm

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

def dame_libros_biblioteca(request, id_biblioteca, texto_libro):
    libros = Libro.objects.select_related("bliblioteca").prefetch_related("autores")
    libros = libros.filter(bliblioteca = id_biblioteca).filter(descripcion__contains=texto_libro).order_by("-nombre")
    return render(request, "libro/lista.html", {"libros_mostrar":libros})

def dame_ultimo_cliente_libro(request, libro):
    cliente = Cliente.objects.filter(prestamo__libro=libro).order_by("-prestamo__fecha_prestamo")[:1].get()
    return render(request, "cliente/cliente.html", {"cliente":cliente})

def libros_no_prestados(request):
    libros = Libro.objects.select_related("bliblioteca").prefetch_related("autores")
    libros = libros.filter(prestamo=None)
    return render(request, "libro/lista.html", {"libros_mostrar":libros})

def mi_error_404(request, exception = None):
    return render(request, "errores/404.html", None, None, 404)





def libro_create(request):
    datosFormulario = None
    if request.method == "POST":
        datosFormulario = request.POST
    formulario = LibroModelForm(datosFormulario)
    
    if (request.method == "POST"):
        libro_creado = crear_libro_modelo(formulario)
        if (libro_creado):
            return redirect("lista_libros")
    return render(request, "libro/create2.html",{"formulario":formulario})
        
        

def crear_libro_modelo(formulario):
    libro_creado = False
    
    if formulario.is_valid():
        try:
            formulario.save()
            libro_creado = True
            
        except Exception as error:
            print(error)
    return libro_creado