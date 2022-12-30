from django.shortcuts import render, redirect

# Create your views here.
from .models import *
from .forms import *

from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required #para vistas basadas en funciones DEF 


from AppMensajeria.models import Mensajes

def inicio(request):
      articulos = Blog.objects.all().order_by('-fecha_publicacion')
      return render(request, 'AppBlog/index.html', {'articulos':articulos, 'avatar':obtenerAvatar(request)})
    
def about(request):
    return render(request, 'AppBlog/about.html', {'avatar':obtenerAvatar(request)})

login_required #Necesario para que solo puedan publicar aquellos que esten logeados
def  crearArticulo(request):
    
    if request.method == 'POST' and request.FILES['imagen']:

        form = BlogForm(request.POST, request.FILES)
        print(request.FILES)
        if form.is_valid():
            ObjectBlog = Blog()
            ObjectBlog.titulo = form.cleaned_data['titulo']
            ObjectBlog.subtitulo = form.cleaned_data['subtitulo']
            ObjectBlog.fecha_publicacion = form.cleaned_data['fecha_publicacion']
            ObjectBlog.contenido = form.cleaned_data['contenido']
            ObjectBlog.imagen = form.cleaned_data['imagen']
            ObjectBlog.usuarioFK = request.user
            ObjectBlog.save()
            return render(request, 'AppBlog/crearArticulo.html', { 'form':form, 'mensaje':'Articulo Cargado Correctamente', 'avatar':obtenerAvatar(request)})
        else:
            form = BlogForm(initial={})
            return render(request, 'AppBlog/crearArticulo.html', { 'form':form, 'mensaje':'Error al Cargar el Articulo', 'avatar':obtenerAvatar(request)})

    else:
        form = BlogForm(initial={})
        
    return render(request, 'AppBlog/crearArticulo.html', {'form':form, 'avatar': obtenerAvatar(request)} )


def articulos(request):
    articulos = Blog.objects.all().order_by('-fecha_publicacion')
    return render(request, 'AppBlog/articulos.html', {'articulos':articulos, 'avatar':obtenerAvatar(request)})

@login_required
def editarArticulo(request, ide):
    if request.method == 'POST':
        articulo = Blog.objects.get(ide=ide)
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            articulo.titulo = form.cleaned_data['titulo']
            articulo.subtitulo = form.cleaned_data['subtitulo']
            articulo.fecha_publicacion = form.cleaned_data['fecha_publicacion']
            articulo.contenido = form.cleaned_data['contenido']
            articulo.imagen = form.cleaned_data['imagen']
            articulo.save()
            return render(request, 'AppBlog/editarArticulo.html', {'form':form, 'mensaje':'Articulo editado Correctamente', 'articulo':articulo, 'avatar':obtenerAvatar(request)})
        else:
            return render(request, 'AppBlog/editarArticulo.html', {'form':form, 'mensaje':'Error al Editar el Articulo', 'articulo':articulo, 'avatar':obtenerAvatar(request)})
    else:
        articulo = Blog.objects.get(ide=ide)
        form = BlogForm(initial={'titulo':articulo.titulo, 'subtitulo': articulo.subtitulo, 'fecha_publicacion':articulo.fecha_publicacion, 'contenido':articulo.contenido, 'imagen':articulo.imagen})
        return render(request, 'AppBlog/editarArticulo.html', {'form':form, 'mensaje':'Articulo editado correctamente', 'articulo':articulo, 'avatar':obtenerAvatar(request)})


def detalleArticulo(request, ide):
    if request.method == 'GET':
        blog = Blog.objects.filter(ide=ide)
        if blog:
            articulo = Blog.objects.get(ide=ide)
            fecha = articulo.fecha_publicacion.strftime("%d %B, %Y")
            user = articulo.usuarioFK
            autor = User.objects.get(username=user)
            return render(request, 'AppBlog/detalleArticulo.html', {'articulo':articulo ,'fecha_format':fecha, 'autor':autor, 'avatar':obtenerAvatar(request) } )
        else:
            return render(request, 'AppBlog/detalleArticulo.html', {'mensaje':'No hay mas Articulos Aun', 'avatar':obtenerAvatar(request)} )

    return render(request, 'AppBlog/detalleArticulo.html', {'mensaje':'No hay mas Articulos Aun', 'avatar':obtenerAvatar(request)})

@login_required
def eliminarArticulo(request, ide):
    if request.method == 'GET':
        articulo = Blog.objects.get(ide=ide)
        articulo.delete()
        return render(request, 'AppBlog/articulos.html', {'mensaje':'Articulo Eliminado Correctamente', 'avatar':obtenerAvatar(request)})
    else:
        return render(request, 'AppBlog/articulos.html', {'mensaje':'NO se pudo eliminar el Articulo', 'avatar':obtenerAvatar(request)})

def login_request(request):
    if request.method == 'POST':
        form = AuthUsuario(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('perfil') #redirecciona a la vista perfilUsuario
            else:
                return render(request, 'AppBlog/login.html', {'form':form, 'mensaje':'Usuario o Contraseña Incorrecta'})
        else:
                return render(request, 'AppBlog/login.html', {'form':form, 'mensaje':'Usuario o Contraseña Incorrecta'})
    else:
        form = AuthUsuario()
    return render(request, 'AppBlog/login.html', {'form':form} )

@login_required #para vistas basadas en funciones DEF
def perfilUsuario(request):
    if request.method == 'POST':
        avatarForm = AvatarForm(request.POST, request.FILES)
        if avatarForm.is_valid():
            ##busco si ya tiene un avatar
            avatarViejo = Avatar.objects.filter(usuarioFK=request.user)
            if len(avatarViejo)!=0:
                avatarViejo[0].delete() #borro el avatar viejo en la segunda columna de la tabla Avatar
            avatar = Avatar(usuarioFK=request.user, imagen=avatarForm.cleaned_data['imagen'] )
            avatar.save()
            avatarForm = AvatarForm()
            tienesMensaje = tienesMensajeNuevo(request)
            return render(request, 'AppBlog/perfil.html' , {'user':request.user , 'avatar':obtenerAvatar(request), 'avatarForm':avatarForm, 'mensaje':'Bienvenido a tu Perfil', 'mensaje_avatar_form':'Imagen de Perfil Actualizada', 'mensajeNuevo':tienesMensaje})
        else:
            avatarForm = AvatarForm()
            tienesMensaje = tienesMensajeNuevo(request)
            return render(request, 'AppBlog/perfil.html' , {'user':request.user ,  'avatar':obtenerAvatar(request), 'avatarForm':avatarForm, 'mensaje':'Bienvenido a tu Perfil', 'mensaje_avatar_form':'Error al Actualizar la Imagen de Perfil', 'mensajeNuevo':tienesMensaje})

    else:
        avatarForm = AvatarForm()
        tienesMensaje = tienesMensajeNuevo(request)
        return render(request, 'AppBlog/perfil.html' , {'user':request.user , 'avatar':obtenerAvatar(request) ,'avatarForm':avatarForm, 'mensaje':'Bienvenido a tu Perfil', 'mensajeNuevo':tienesMensaje})
def editarPerfil(request):
    if request.method == 'POST':
        form = EditartPerfilForm(request.POST)
        if form.is_valid():
            user = request.user
            user.first_name = form.cleaned_data['nombre']
            user.last_name = form.cleaned_data['apellido']
            user.email = form.cleaned_data['email']
            user.save()
            form = EditartPerfilForm()
            return render(request, 'AppBlog/editarPerfil.html', {'form':form, 'mensaje':'Datos Actualizados Correctamente', 'avatar':obtenerAvatar(request)})
        else:
            form = EditartPerfilForm()
            return render(request, 'AppBlog/editarPerfil.html', {'form':form, 'mensaje':'Error al Actualizar los Datos', 'avatar':obtenerAvatar(request)})
    else:
        form = EditartPerfilForm()
    return render(request, 'AppBlog/editarPerfil.html', {'form':form, 'avatar':obtenerAvatar(request)})

def obtenerAvatar(request):
    try:
        lista=Avatar.objects.filter(usuarioFK=request.user) # falla al buscar cuando un usuario no esta logeado, solucionado con try
        if len(lista)!=0:
            imagen=lista[0].imagen.url
        else:
            imagen="/media/avatar/img_avatar.png"
        return imagen
    except:
        return "/media/avatar/img_avatar.png"



def registroUsuario(request):
    if request.method == 'POST':
        form = RegistroUsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'AppBlog/registro.html', {'form':form, 'mensaje':'Usuario Registrado Correctamente', 'avatar':obtenerAvatar(request)})
        else:
            errores = form.errors
            form = RegistroUsuarioForm()    
            return render(request, 'AppBlog/registro.html', {'form':form, 'mensaje':'Error al Registrar el Usuario', 'errores':errores})
    else:
        form = RegistroUsuarioForm()
    return render(request, 'AppBlog/registro.html', {'form':form} )

def tienesMensajeNuevo(request):
    if request.method == 'GET':
        mensajes = Mensajes.objects.filter(userDestinatario=request.user, leido=False)
        if mensajes:
            return True
        else:
            return False
    else:
        return False