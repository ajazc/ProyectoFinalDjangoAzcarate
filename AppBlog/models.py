from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
# Create your models here.

class Blog(models.Model):
    ide = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=100)   
    subtitulo = models.CharField(max_length=100, null=True, blank=True)
    fecha_publicacion = models.DateField()
    contenido = RichTextField()
    imagen=models.ImageField(upload_to='blog/')
    usuarioFK = models.ForeignKey(User, on_delete=models.CASCADE, null=True) #Relacion de uno a muchos
    def __str__(self):
        return self.titulo

    def getContenido(self):
        return self.contenido

    def getFecha(self):
        return self.fecha_publicacion.strftime('%b %e %Y')


class Avatar(models.Model):
    ide = models.AutoField(primary_key=True)
    imagen = models.ImageField(upload_to='avatar/')
    usuarioFK = models.ForeignKey(User, on_delete=models.CASCADE, null=True) #Relacion de uno a muchos

    def __str__(self):
        return self.usuarioFK.username

    def getImagen(self):
        return self.imagen

    def getUsuario(self):
        return self.usuarioFK.username