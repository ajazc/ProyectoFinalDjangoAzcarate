from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Mensajes(models.Model):
    ide = models.AutoField(primary_key=True)
    userRemitente = models.ForeignKey(User, related_name='userRemitente', on_delete=models.CASCADE) #Relacion de uno a muchos
    userDestinatario = models.ForeignKey(User, related_name='userDestinatario', on_delete=models.CASCADE) #Relacion de uno a muchos
    mensaje = models.CharField(max_length=200)
    fecha = models.DateTimeField()
    leido = models.BooleanField(default=False)
    def __str__(self):
        return self.mensaje

    def getMensaje(self):
        return self.mensaje

    def getFecha(self):
        return self.fecha.strftime('%b %e %Y')

    def getRemitente(self):
        return self.userRemitente.username

    def getDestinatario(self):
        return self.userDestinatario.username

    def getLeido(self):
        return self.leido