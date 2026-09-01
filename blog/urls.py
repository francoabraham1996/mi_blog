from django.urls import path
from . import views


urlpatterns = [

    # Página principal
    path('', views.inicio, name='inicio'),

    # Ver un artículo
    path(
        'articulo/<int:pk>/',
        views.detalle,
        name='detalle'
    ),

    # Crear artículo
    path(
        'crear/',
        views.crear,
        name='crear'
    ),

    # Iniciar sesión
    path(
        'login/',
        views.iniciar_sesion,
        name='iniciar_sesion'
    ),

    # Registrarse
    path(
        'registro/',
        views.registrarse,
        name='registrarse'
    ),

    # Cerrar sesión
    path(
        'logout/',
        views.cerrar_sesion,
        name='cerrar_sesion'
    ),

    # Editar articulo
    path(
    'articulo/<int:pk>/editar/',
    views.editar,
    name='editar'
    ),

    # Eliminar articulo
    path(
    'articulo/<int:pk>/eliminar/',
    views.eliminar,
    name='eliminar'
    ),

    # Editar mi perfil
    path(
    'mi-perfil/',
    views.mi_perfil,
    name='mi_perfil'
    ),

    # Acerca de mí
    path(
    'acerca-de/',
    views.acerca_de,
    name='acerca_de'
    ),

    # Contacto
    path(
    'contacto/',
    views.contacto,
    name='contacto'
    ),


]