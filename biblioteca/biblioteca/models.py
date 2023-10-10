from django.db import models
from django.utils import timezone

# Create your models here.

class Biblioteca(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.TextField()
    fechaCreacion = models.DateField(null=True, blank=True)
    telefono = models.IntegerField(null=True, blank=True)
    
    
class Autor(models.Model):
    nombre = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=200,blank=True)
    edad = models.IntegerField(null = True)
    dni = models.CharField(max_length=9, unique=True)
    
    
class Libro(models.Model):
    IDIOMAS = [
        ("ES", "Español"),
        ("EN", "Inglés"),
        ("FR", "Francés"),
        ("IT", "Italiano"),
    ]
    
    nombre = models.CharField(max_length=200)
    idioma = models.CharField(
        max_length=2,
        choices=IDIOMAS,
        default="ES",
        )
    descripcion = models.TextField()
    fecha_publicacion = models.DateField()
    GENEROS = [
        ("AV", "Aventuras"),
        ("CF", "Ciencia Ficción"),
        ("TE", "Terror"),
        ("RO", "Romántica"),
        ("HU", "Humor"),
    ]
    genero = models.CharField(
        max_length=2,
        choices=GENEROS,
        )
    isbn = models.IntegerField()
    bliblioteca = models.ForeignKey(Biblioteca, on_delete=models.CASCADE)
    autores = models.ManyToManyField(Autor)
    
class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    apellidos =  apellidos = models.CharField(max_length=100)
    email = models.CharField(max_length=200,unique=True)
    puntos = models.FloatField(default=5.0,db_column="puntos_biblioteca")
    telefono = models.IntegerField()
    
class DatosCliente(models.Model):
    direccion = models.TextField()
    gustos = models.TextField()
    telefono = models.IntegerField()
    altura = models.FloatField(null=True, blank=True)
    peso = models.FloatField(null=True, blank=True)
    dni = models.CharField(max_length=9, unique=True)
    cliente = models.OneToOneField(Cliente, on_delete=models.CASCADE)
    
    
class Prestamo(models.Model):
    cliente = models.ForeignKey(Cliente,on_delete=models.CASCADE)
    libro = models.ForeignKey(Libro, on_delete=models.CASCADE)
    fecha_prestamo = models.DateTimeField(default=timezone.now)
    