from django.test import TestCase
from .models import Contacto

class ContactoModelTest(TestCase):
    def test_creacion_contacto(self):
        contacto = Contacto.objects.create(
            nombre_apellido='Juan Pérez',
            es_usuario=True,
            email='juan@example.com',
            tipo_consulta='reclamo',
            mensaje='Esto es un reclamo de prueba.'
        )
        self.assertEqual(contacto.nombre_apellido, 'Juan Pérez')
        self.assertEqual(contacto.tipo_consulta, 'reclamo')
        self.assertTrue(contacto.es_usuario)
