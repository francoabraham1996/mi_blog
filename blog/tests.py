from django.test import TestCase
from django.urls import reverse


class BlogTests(TestCase):

    # ==========================================
    # TEST DE LA PÁGINA PRINCIPAL
    # ==========================================

    def test_inicio(self):

        respuesta = self.client.get(
            reverse('inicio')
        )

        self.assertEqual(
            respuesta.status_code,
            200
        )


    # ==========================================
    # TEST DE ACERCA DE MÍ
    # ==========================================

    def test_acerca_de(self):

        respuesta = self.client.get(
            reverse('acerca_de')
        )

        self.assertEqual(
            respuesta.status_code,
            200
        )


    # ==========================================
    # TEST DE CONTACTO
    # ==========================================

    def test_contacto(self):

        respuesta = self.client.get(
            reverse('contacto')
        )

        self.assertEqual(
            respuesta.status_code,
            200
        )


    # ==========================================
    # TEST DE CREAR ARTÍCULO SIN LOGIN
    # ==========================================

    def test_crear_requiere_login(self):

        respuesta = self.client.get(
            reverse('crear')
        )

        self.assertEqual(
            respuesta.status_code,
            302
        )