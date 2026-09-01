from django.db import models
from django.contrib.auth import get_user_model


# Obtenemos el modelo de usuario que utiliza Django.
User = get_user_model()


# ==========================================
# MODELO ARTÍCULO
# ==========================================

class Articulo(models.Model):

    # Título del artículo.
    # Puede tener como máximo 200 caracteres.
    titulo = models.CharField(
        max_length=200
    )

    # Contenido completo del artículo.
    contenido = models.TextField()

    # Usuario que creó el artículo.
    #
    # ForeignKey significa que:
    # un usuario puede tener muchos artículos.
    #
    # Si eliminamos el usuario,
    # también se eliminan sus artículos.
    autor = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    # Guarda automáticamente la fecha
    # en la que se creó el artículo.
    creado = models.DateTimeField(
        auto_now_add=True
    )

    # Se actualiza automáticamente
    # cada vez que modificamos el artículo.
    actualizado = models.DateTimeField(
        auto_now=True
    )

    # Así se mostrará el artículo
    # dentro del administrador de Django.
    def __str__(self):
        return self.titulo


# ==========================================
# MODELO PERFIL
# ==========================================

class Perfil(models.Model):

    # Cada usuario puede tener UN solo perfil.
    #
    # OneToOneField:
    #
    # Usuario 1  ←→  Perfil 1
    #
    # Si eliminamos el usuario,
    # también se elimina su perfil.
    usuario = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )

    # Biografía del usuario.
    #
    # blank=True significa que
    # no es obligatorio completarla.
    biografia = models.TextField(
        blank=True
    )

    # Así aparecerá el perfil
    # dentro del administrador de Django.
    def __str__(self):
        return f'Perfil de {self.usuario.username}'

# ==========================================
# MODELO MENSAJE DE CONTACTO
# ==========================================

class MensajeContacto(models.Model):

    # Nombre de la persona que envía el mensaje.
    nombre = models.CharField(
        max_length=100
    )

    # Email de contacto.
    email = models.EmailField()

    # Mensaje escrito por el usuario.
    mensaje = models.TextField()

    # Fecha en la que se envió el mensaje.
    creado = models.DateTimeField(
        auto_now_add=True
    )

    # Así se mostrará en el administrador.
    def __str__(self):
        return f'{self.nombre} - {self.email}'
        