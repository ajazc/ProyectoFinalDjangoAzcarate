from ckeditor.widgets import CKEditorWidget
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UsernameField

class MensajeForm(forms.Form):
    contenido = forms.CharField(required=True, label='Mensaje', widget=forms.Textarea(attrs={'class':'form-control', 'placeholder':'Escribe tu mensaje', 'rows':'3', 'cols':'5'}))
    