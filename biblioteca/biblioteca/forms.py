from django import forms
from .models import Libro, Biblioteca, Autor
import datetime
from django.forms import ModelForm

class LibroForms(forms.Form):
    
    #Definimos un campo de tipo Texto para el nombre
    nombre = forms.CharField(label="Nombre del Libro",
                             required=True, 
                             max_length=200,
                             help_text="200 caracteres como máximo")
    
    #Definimos un campo de Tipo Textarea para la descripcion
    descripcion = forms.CharField(label="Descripcion",
                                  required=False,
                                  widget=forms.Textarea())
    
    #Definimos un campo de Tipo Fecha para la fecha de publicación
    fecha_publicacion = forms.DateField(label="Fecha Publicación",
                                        initial=datetime.date.today,
                                        widget= forms.SelectDateWidget()
                                        )
    
    #Definimos un campo Select para seleccionar el Idioma
    idioma = forms.ChoiceField(choices=Libro.IDIOMAS,
                               initial="ES")
    
    #Definimos un campo Select para seleccionar una biblioteca que es una relacion ManyToOne
    bibliotecasDisponibles = Biblioteca.objects.all()
    biblioteca = forms.ModelChoiceField(
            queryset=bibliotecasDisponibles,
            widget=forms.Select,
            required=True,
            empty_label="Ninguna"
    )
    
     #Definimos un campo Select Múltiple para seleccionar autores en una relación ManyToMany
    autoresDisponibles = Autor.objects.all()
    autores = forms.ModelMultipleChoiceField(
        queryset= autoresDisponibles,
        required=True,
        help_text="Mantén pulsada la tecla control para seleccionar varios elementos"
    )
    
class LibroModelForm(ModelForm):   
    class Meta:
        model = Libro
        fields = ['nombre','isbn','descripcion','fecha_publicacion','idioma','bliblioteca','autores']
        labels = {
            "nombre": ("Nombre del Libro"),
        }
        help_texts = {
            "nombre": ("200 caracteres como máximo"),
            "autores":("Mantén pulsada la tecla control para seleccionar varios elementos")
        }
        widgets = {
            "fecha_publicacion":forms.SelectDateWidget()
        }
        localized_fields = ["fecha_publicacion"]