from ckeditor.widgets import CKEditorWidget
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Blog
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UsernameField


class BlogForm(forms.Form):

    titulo = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control", "placeholder":" Ingrese el Titulo"}), 
                                                                            help_text=("El titulo debe tener Maximo 50 caracteres"), 
                                                                                max_length=100, required=True)

    subtitulo = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control", "placeholder":" Ingrese el Subtitulo"}), 
                                                                            help_text=("El subtitulo debe tener Maximo 50 caracteres"),
                                                                             max_length=100, required=True)

    fecha_publicacion = forms.DateTimeField(widget=forms.TextInput(attrs={"class":"form-control", "type":"date"}) , required=True)

    contenido = forms.CharField(widget=CKEditorWidget())
    
    class Meta:
        model = Blog
        fields = ('titulo', 'fecha_publicacion', 'contenido', 'imagen', 'subtitulo', 'usuarioFK')
        widgets = {
            'contenido': CKEditorWidget(),
        }
    
    imagen = forms.ImageField(label="Imagen", widget=forms.FileInput(attrs={"class":"form-control"}), required=True)

class RegistroUsuarioForm(UserCreationForm):
    username = forms.CharField(label="Nombre de Usuario", 
                                widget=forms.TextInput(attrs={"class":"form-control", "placeholder":" Ingrese el Nombre de Usuario", "required":True, "autofocus":True, "class":"form-control"}),
                                help_text=("El nombre de usuario debe tener al menos 4 caracteres")
                                )
    email = forms.EmailField(widget=forms.TextInput(attrs={"class":"form-control", "placeholder":" Ingrese el Email","class":"form-control"}),
                            help_text=("Ingrese un email valido"))
    password1= forms.CharField(label="Ingrese Contraseña",
                                widget=forms.PasswordInput(attrs={"class":"form-control", "placeholder":" Ingrese la Contraseña", "class":"form-control"}),
                                help_text=("La contraseña debe tener al menos 8 caracteres, al menos 1 letra, al menos 1 número y no puede ser una contraseña común."))

    password2= forms.CharField(label="Repita Contraseña", 
                                widget=forms.PasswordInput(attrs={"class":"form-control", "placeholder":" Repita la Contraseña", "class":"form-control"}),
                                help_text=("Ingrese la misma contraseña para verificación."))

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

class AuthUsuario(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={"autofocus": True , "class":"form-control", "placeholder":" Ingrese el Nombre de Usuario"}))
    password = forms.CharField(
        label=("Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "current-password", "class":"form-control", "placeholder":" Ingrese la Contraseña"})
    )

class EditartPerfilForm(forms.Form):
    nombre = forms.CharField(label="Nombre",widget=forms.TextInput(attrs={"class":"form-control", "placeholder":" Ingrese el Nombre"}), required=True, max_length=10)

    apellido = forms.CharField(label="Apellido",widget=forms.TextInput(attrs={"class":"form-control", "placeholder":" Ingrese el Apellido"}), required=True, max_length=10)
    
    email = forms.EmailField(widget=forms.TextInput(attrs={"class":"form-control", "placeholder":" Ingrese el Email","class":"form-control"}),
                            help_text=("Ingrese un email valido"))
    class Meta:
        model = User
        fields = ["first_name", "last_name", "username","email", ]

class AvatarForm(forms.Form):
    imagen = forms.ImageField(label="Imagen", widget=forms.FileInput(attrs={"class":"form-control"}), required=True)