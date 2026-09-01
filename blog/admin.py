from django.contrib import admin
from .models import Articulo, Perfil, MensajeContacto


# ==========================================
# ADMINISTRACIÓN DE ARTÍCULOS
# ==========================================

@admin.register(Articulo)
class ArticuloAdmin(admin.ModelAdmin):

    # Columnas que vamos a ver en el listado
    list_display = (
        'titulo',
        'autor',
        'creado',
        'actualizado',
    )

    # Buscador del administrador
    search_fields = (
        'titulo',
        'contenido',
        'autor__username',
    )

    # Filtros laterales
    list_filter = (
        'creado',
        'autor',
    )


# ==========================================
# ADMINISTRACIÓN DE PERFILES
# ==========================================

@admin.register(Perfil)
class PerfilAdmin(admin.ModelAdmin):

    # Mostramos el usuario del perfil
    list_display = (
        'usuario',
    )

    # Podemos buscar perfiles por usuario
    search_fields = (
        'usuario__username',
    )


# ==========================================
# ADMINISTRACIÓN DE MENSAJES DE CONTACTO
# ==========================================

@admin.register(MensajeContacto)
class MensajeContactoAdmin(admin.ModelAdmin):

    # Columnas del listado
    list_display = (
        'nombre',
        'email',
        'creado',
    )

    # Podemos buscar por nombre, email o mensaje
    search_fields = (
        'nombre',
        'email',
        'mensaje',
    )

    # Podemos filtrar por fecha
    list_filter = (
        'creado',
    )