from django.shortcuts import render , redirect

from django.contrib.auth.decorators import login_required
# Create your views here.

from AppBlog.views import obtenerAvatar

from .models import *

from .forms import *



import datetime


@login_required
def inicioMensajes(request, id=None):
    if request.method == 'GET':
        remitente = request.user #id del usuario que envia el mensaje
        if id != None: #id del usuario que recibe el mensaje
            destinatario = User.objects.get(id=id) #usuario que recibe el mensaje
            formMensaje = MensajeForm() #formulario para enviar mensaje
            usuarios = User.objects.all() #lista de usuarios para enviar mensaje
            chat = obtenerConversacion(request, remitente, destinatario)
            return render(request, 'AppMensajeria/inicio.html', {'usuarios':usuarios, 'avatar':obtenerAvatar(request) , 'formMensaje':formMensaje, 'destinatario': destinatario, 'chat':chat})
        else:
            formMensaje = MensajeForm()
            usuarios = User.objects.all()
            
    elif request.method == 'POST':
        formMensaje = MensajeForm(request.POST)
        
        if formMensaje.is_valid() and id != None:
            contenido = formMensaje.cleaned_data['contenido']
            remitente = request.user
            destinatario = request.POST.get('destinatario')
            mensaje = Mensajes()
            mensaje.userRemitente = remitente
            mensaje.userDestinatario = User.objects.get(id=destinatario)
            mensaje.mensaje = contenido
            mensaje.fecha = datetime.datetime.now()

            mensaje.save()
            formMensaje = MensajeForm()
            usuarios = User.objects.all()
            return render(request, 'AppMensajeria/inicio.html', {'usuarios':usuarios, 'avatar':obtenerAvatar(request) , 'formMensaje':formMensaje, 'mensaje':'Mensaje enviado correctamente'})
        else:
            formMensaje = MensajeForm()
            usuarios = User.objects.all()
            return render(request, 'AppMensajeria/inicio.html', {'usuarios':usuarios, 'avatar':obtenerAvatar(request) , 'formMensaje':formMensaje, 'mensaje':'Error al enviar el mensaje, Formulario no valido'})
    return render(request, 'AppMensajeria/inicio.html', {'usuarios':usuarios, 'avatar':obtenerAvatar(request) , 'formMensaje':formMensaje})

def obtenerConversacion(request, remitente, destinatario):
    chat = Mensajes.objects.filter(userRemitente=remitente, userDestinatario=destinatario) | Mensajes.objects.filter(userRemitente=destinatario, userDestinatario=remitente).order_by('fecha')
    return chat

def marcarLeido(request, id=None):
    if request.method == 'GET':
        if id != None:
            mensaje = Mensajes.objects.filter(ide=id)
            mensaje.update(leido=True)           
            
            return redirect('mensajes')
        else:
            return redirect('mensajes')
    else:
        return redirect('mensajes')

def tienesMensajeNuevo(request):
    if request.method == 'GET':
        mensajes = Mensajes.objects.filter(userDestinatario=request.user, leido=False)
        if mensajes:
            return True
        else:
            return False
    else:
        return False