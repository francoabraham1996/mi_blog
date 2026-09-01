from django import forms
from .models import Articulo, Perfil, MensajeContacto


class ArticuloForm(forms.ModelForm):

    class Meta:
        model = Articulo

        fields = ('titulo', 'contenido')

        widgets = {
            'titulo': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Título del artículo'
                }
            ),

            'contenido': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'rows': 10,
                    'placeholder': 'Escribe el contenido aquí...'
                }
            ),
        }

class PerfilForm(forms.ModelForm):

    class Meta:
        model = Perfil

        fields = [
            'biografia',
        ]

        widgets = {
            'biografia': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'rows': 5,
                    'placeholder': 'Contanos algo sobre vos...'
                }
            ),
        }

# ==========================================
# FORMULARIO DE CONTACTO
# ==========================================

class ContactoForm(forms.ModelForm):

    class Meta:

        model = MensajeContacto

        fields = [
            'nombre',
            'email',
            'mensaje',
        ]

        widgets = {

            'nombre': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Tu nombre'
                }
            ),

            'email': forms.EmailInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'tuemail@ejemplo.com'
                }
            ),

            'mensaje': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'rows': 6,
                    'placeholder': 'Escribí tu mensaje...'
                }
            ),

        }