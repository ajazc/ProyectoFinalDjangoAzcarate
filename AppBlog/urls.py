from django.urls import path, include
from AppBlog.views import *
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path("", inicio, name='inicio'),
    path("about/", about, name="about"),
    path("articulo/add",crearArticulo, name="crearArticulo"),
    path("articulos/", articulos, name="articulos"),
    path("articulos/<ide>", detalleArticulo, name="detalleArticulo"),
    path("articulos/editar/<ide>", editarArticulo, name="editarArticulo"),
    path("articulos/eliminar/<ide>", eliminarArticulo, name="eliminarArticulo"),
    path('ckeditor', include('ckeditor_uploader.urls')),

    path("login/", login_request, name='login'),
    path("logout/", LogoutView.as_view(), name='logout'),
    path("registro/", registroUsuario, name='registro'),
    path("perfil/", perfilUsuario, name='perfil'),
    path("perfil/editar", editarPerfil, name='editarPerfil'),
    path("mensajes/", include('AppMensajeria.urls'), name='mensajes'),
    
]



